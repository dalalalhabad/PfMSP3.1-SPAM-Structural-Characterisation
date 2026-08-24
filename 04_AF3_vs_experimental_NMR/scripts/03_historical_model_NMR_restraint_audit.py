from pathlib import Path
import re
import csv
import numpy as np
from openmm import app, unit

ROOT = Path("04_AF3_vs_experimental_NMR")

MR = ROOT / "input/NMR_experimental_data/1PSM.mr"

PDB = (
    ROOT /
    "results/hydrogenated_historical/"
    "model.B99990034_H.pdb"
)

RESULTS = ROOT / "results"

# ------------------------------------------------------------
# Parse deposited distance restraints
# ------------------------------------------------------------

lines = MR.read_text().splitlines()

dihedral_start = next(
    i for i, line in enumerate(lines)
    if re.search(r"restraints\s+dihedral", line, re.I)
)

pattern = re.compile(
    r'assign\s+'
    r'\(resid\s+(\d+)\s+and\s+name\s+([^\)]+)\)\s+'
    r'\(resid\s+(\d+)\s+and\s+name\s+([^\)]+)\)\s+'
    r'([-0-9.]+)\s+([-0-9.]+)\s+([-0-9.]+)',
    re.I
)

restraints = []

for lineno, line in enumerate(lines[:dihedral_start], 1):

    m = pattern.search(line)

    if not m:
        continue

    r1 = int(m.group(1))
    a1 = m.group(2).strip().upper()

    r2 = int(m.group(3))
    a2 = m.group(4).strip().upper()

    target = float(m.group(5))
    minus = float(m.group(6))
    plus = float(m.group(7))

    restraints.append({
        "source_line": lineno,
        "nmr_r1": r1,
        "a1": a1,
        "nmr_r2": r2,
        "a2": a2,
        "hist_r1": r1 + 6,
        "hist_r2": r2 + 6,
        "separation": abs(r2-r1),
        "lower": target - minus,
        "upper": target + plus,
    })

# ------------------------------------------------------------
# Classify restraint type
# ------------------------------------------------------------

def restraint_class(a1, a2):

    names = [a1, a2]

    if any("#" in x for x in names):
        return "pseudoatom_group"

    if any(
        re.fullmatch(r"H[BGDE][12]", x)
        for x in names
    ):
        return "legacy_stereospecific"

    return "direct_unambiguous"

for r in restraints:
    r["restraint_class"] = restraint_class(
        r["a1"],
        r["a2"]
    )

# ------------------------------------------------------------
# Coordinates
# ------------------------------------------------------------

structure = app.PDBFile(str(PDB))

coords = {}

for atom in structure.topology.atoms():

    resid = int(atom.residue.id)
    name = atom.name.upper()

    xyz = structure.positions[
        atom.index
    ].value_in_unit(unit.angstrom)

    coords[(resid, name)] = np.asarray(
        xyz,
        dtype=float
    )

# ------------------------------------------------------------
# XPLOR -> OpenMM proton names
# ------------------------------------------------------------

def candidates(resid, name):

    name = name.upper()

    if name == "HN":
        names = ["H"]

    elif name in {
        "HA", "HB", "HG",
        "HE21", "HE22",
        "HD21", "HD22",
        "OD1"
    }:
        names = [name]

    elif name == "HB1":
        names = ["HB2"]

    elif name == "HB2":
        names = ["HB3"]

    elif name == "HG1":
        names = ["HG2"]

    elif name == "HG2":
        names = ["HG3"]

    elif name == "HD1":
        names = ["HD2"]

    elif name == "HD2":
        names = ["HD3"]

    elif name == "HE1":
        names = ["HE2"]

    elif name == "HE2":
        names = ["HE3"]

    elif name == "HB#":
        names = ["HB1", "HB2", "HB3"]

    elif name == "HG#":
        names = [
            "HG", "HG1", "HG2", "HG3",
            "HG11", "HG12", "HG13",
            "HG21", "HG22", "HG23"
        ]

    elif name == "HD#":
        names = [
            "HD", "HD1", "HD2", "HD3",
            "HD11", "HD12", "HD13",
            "HD21", "HD22", "HD23"
        ]

    elif name == "HE#":
        names = [
            "HE", "HE1", "HE2", "HE3",
            "HE21", "HE22"
        ]

    elif name == "HZ#":
        names = [
            "HZ", "HZ1", "HZ2", "HZ3"
        ]

    elif name == "HG1#":
        names = ["HG11", "HG12", "HG13"]

    elif name == "HG2#":
        names = ["HG21", "HG22", "HG23"]

    elif name == "HD1#":
        names = ["HD11", "HD12", "HD13"]

    elif name == "HD2#":
        names = ["HD21", "HD22", "HD23"]

    else:
        names = [name]

    return [
        n for n in names
        if (resid, n) in coords
    ]

# ------------------------------------------------------------
# Evaluate
# ------------------------------------------------------------

rows = []

sat = 0
viol = 0
missing = 0

for r in restraints:

    c1 = candidates(
        r["hist_r1"],
        r["a1"]
    )

    c2 = candidates(
        r["hist_r2"],
        r["a2"]
    )

    if not c1 or not c2:

        status = "NOT_EVALUATED"

        dmin = np.nan
        atom1 = ""
        atom2 = ""

        upper_violation = np.nan

        missing += 1

    else:

        values = []

        for a in c1:
            for b in c2:

                d = np.linalg.norm(
                    coords[(r["hist_r1"], a)] -
                    coords[(r["hist_r2"], b)]
                )

                values.append(
                    (d, a, b)
                )

        values.sort()

        dmin, atom1, atom2 = values[0]

        upper_violation = max(
            0.0,
            dmin - r["upper"]
        )

        if (
            r["lower"]
            <= dmin
            <= r["upper"]
        ):

            status = "SATISFIED"
            sat += 1

        else:

            status = "VIOLATED"
            viol += 1

    rows.append({
        "Source_line": r["source_line"],
        "NMR_residue_1": r["nmr_r1"],
        "NMR_atom_1": r["a1"],
        "NMR_residue_2": r["nmr_r2"],
        "NMR_atom_2": r["a2"],
        "Historical_residue_1": r["hist_r1"],
        "Historical_residue_2": r["hist_r2"],
        "Sequence_separation": r["separation"],
        "Restraint_class": r["restraint_class"],
        "Lower_bound_A": r["lower"],
        "Upper_bound_A": r["upper"],
        "Historical_distance_A": dmin,
        "Historical_atom_1": atom1,
        "Historical_atom_2": atom2,
        "Upper_violation_A": upper_violation,
        "Status": status
    })

evaluated = sat + viol

print("===== HISTORICAL MODEL vs NMR RESTRAINTS =====")
print("Deposited restraints:", len(restraints))
print("Evaluated:", evaluated)
print("Satisfied:", sat)
print("Violated:", viol)
print("Not evaluated:", missing)

if evaluated:
    print(
        f"Satisfaction: "
        f"{100*sat/evaluated:.2f}%"
    )

# Save detailed results

detail = (
    RESULTS /
    "Historical_model_vs_all_experimental_distance_restraints.csv"
)

with detail.open("w", newline="") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(rows)

# ------------------------------------------------------------
# Compare specifically against 5/5 AF3 consensus violations
# ------------------------------------------------------------

consensus_file = (
    RESULTS /
    "AF3_consensus_violation_summary.csv"
)

consensus = list(
    csv.DictReader(
        consensus_file.open()
    )
)

consensus5 = {
    int(r["Source_line"]): r
    for r in consensus
    if int(r["Models_violated"]) == 5
}

comparison = []

print()
print("===== AF3 5/5 CONSENSUS FAILURES vs HISTORICAL MODEL =====")

for row in rows:

    source = int(row["Source_line"])

    if source not in consensus5:
        continue

    af3 = consensus5[source]

    hist_status = row["Status"]

    if hist_status == "SATISFIED":
        outcome = "HISTORICAL_RESOLVES_AF3_CONSENSUS_VIOLATION"
    elif hist_status == "VIOLATED":
        outcome = "BOTH_AF3_AND_HISTORICAL_VIOLATE"
    else:
        outcome = "HISTORICAL_NOT_EVALUATED"

    comparison.append({
        "Source_line": source,
        "NMR_residue_1": row["NMR_residue_1"],
        "NMR_atom_1": row["NMR_atom_1"],
        "NMR_residue_2": row["NMR_residue_2"],
        "NMR_atom_2": row["NMR_atom_2"],
        "Sequence_separation": row["Sequence_separation"],
        "Restraint_class": row["Restraint_class"],
        "Upper_bound_A": row["Upper_bound_A"],
        "AF3_mean_distance_A": af3["Mean_distance_A"],
        "AF3_mean_violation_A": af3["Mean_upper_violation_A"],
        "Historical_distance_A": row["Historical_distance_A"],
        "Historical_upper_violation_A": row["Upper_violation_A"],
        "Historical_status": hist_status,
        "Outcome": outcome
    })

    print()
    print(
        f"NMR {row['NMR_residue_1']} {row['NMR_atom_1']} "
        f"↔ {row['NMR_residue_2']} {row['NMR_atom_2']}"
    )

    print(
        f"AF3 mean distance: "
        f"{float(af3['Mean_distance_A']):.3f} Å"
    )

    print(
        f"Historical distance: "
        f"{float(row['Historical_distance_A']):.3f} Å"
    )

    print(
        f"Upper bound: "
        f"{float(row['Upper_bound_A']):.2f} Å"
    )

    print("Historical status:", hist_status)
    print("Outcome:", outcome)

comp_path = (
    RESULTS /
    "AF3_consensus_violations_vs_historical_model.csv"
)

with comp_path.open("w", newline="") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=comparison[0].keys()
    )

    writer.writeheader()
    writer.writerows(comparison)

print()
print("Saved:")
print(detail)
print(comp_path)

