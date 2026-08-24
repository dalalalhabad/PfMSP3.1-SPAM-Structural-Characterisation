from pathlib import Path
import re
import csv
from collections import Counter, defaultdict

import numpy as np
from openmm import app, unit


ROOT = Path("04_AF3_vs_experimental_NMR")

MR_FILE = ROOT / "input/NMR_experimental_data/1PSM.mr"

PDB_DIR = ROOT / "results/hydrogenated_AF3"

OUT_DIR = ROOT / "results"
OUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 1. Parse deposited experimental distance restraints
# ============================================================

lines = MR_FILE.read_text().splitlines()

dihedral_start = next(
    i for i, line in enumerate(lines)
    if re.search(r"restraints\s+dihedral", line, re.I)
)

distance_lines = lines[:dihedral_start]

pattern = re.compile(
    r'assign\s+'
    r'\(resid\s+(\d+)\s+and\s+name\s+([^\)]+)\)\s+'
    r'\(resid\s+(\d+)\s+and\s+name\s+([^\)]+)\)\s+'
    r'([-0-9.]+)\s+([-0-9.]+)\s+([-0-9.]+)',
    re.I
)

restraints = []

for lineno, line in enumerate(distance_lines, 1):

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

    # For these deposited XPLOR restraints:
    # target = 0
    # minus is negative
    # plus is the upper distance limit.
    lower = target - minus
    upper = target + plus

    separation = abs(r2 - r1)

    restraints.append({
        "source_line": lineno,
        "nmr_r1": r1,
        "nmr_a1": a1,
        "nmr_r2": r2,
        "nmr_a2": a2,
        "af3_r1": r1 + 6,
        "af3_r2": r2 + 6,
        "separation": separation,
        "lower": lower,
        "upper": upper,
    })


print("===== DEPOSITED DISTANCE RESTRAINTS =====")
print("Parsed:", len(restraints))

sep_counts = Counter(r["separation"] for r in restraints)

for sep in sorted(sep_counts):

    label = (
        "intra-residue"
        if sep == 0
        else f"i→i+{sep}"
    )

    print(f"{label:16s}: {sep_counts[sep]}")


# ============================================================
# 2. Classify restraint type
# ============================================================

def restraint_class(atom1, atom2):

    names = [atom1.upper(), atom2.upper()]

    if any("#" in x for x in names):
        return "pseudoatom_group"

    # These legacy XPLOR proton names can require
    # stereospecific nomenclature translation.
    if any(
        re.fullmatch(r"H[BGDE][12]", x)
        for x in names
    ):
        return "legacy_stereospecific"

    return "direct_unambiguous"


for r in restraints:
    r["restraint_class"] = restraint_class(
        r["nmr_a1"],
        r["nmr_a2"]
    )


print("\n===== RESTRAINT CLASSES =====")

class_counts = Counter(
    r["restraint_class"] for r in restraints
)

for name, n in sorted(class_counts.items()):
    print(f"{name:24s}: {n}")


# ============================================================
# 3. Read hydrogenated model coordinates
# ============================================================

def read_coords(pdb_path):

    structure = app.PDBFile(str(pdb_path))

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

    return coords


# ============================================================
# 4. XPLOR proton nomenclature -> OpenMM atom candidates
# ============================================================

def atom_candidates(coords, resid, xplor_name):

    name = xplor_name.upper()

    # Backbone amide proton
    if name == "HN":
        names = ["H"]

    # Directly equivalent names
    elif name in {
        "HA", "HB", "HG",
        "HE21", "HE22",
        "HD21", "HD22",
    }:
        names = [name]

    # Legacy XPLOR stereospecific naming.
    #
    # These mappings are retained as a screening convention
    # and should not be interpreted as experimentally
    # stereospecific validation without further confirmation.
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

    # Pseudoatom groups
    elif name == "HB#":
        names = [
            "HB1", "HB2", "HB3"
        ]

    elif name == "HG#":
        names = [
            "HG", "HG1", "HG2", "HG3",
            "HG11", "HG12", "HG13",
            "HG21", "HG22", "HG23",
        ]

    elif name == "HD#":
        names = [
            "HD", "HD1", "HD2", "HD3",
            "HD11", "HD12", "HD13",
            "HD21", "HD22", "HD23",
        ]

    elif name == "HE#":
        names = [
            "HE", "HE1", "HE2", "HE3",
            "HE21", "HE22",
        ]

    elif name == "HZ#":
        names = [
            "HZ", "HZ1", "HZ2", "HZ3"
        ]

    elif name == "HG1#":
        names = [
            "HG11", "HG12", "HG13"
        ]

    elif name == "HG2#":
        names = [
            "HG21", "HG22", "HG23"
        ]

    elif name == "HD1#":
        names = [
            "HD11", "HD12", "HD13"
        ]

    elif name == "HD2#":
        names = [
            "HD21", "HD22", "HD23"
        ]

    else:
        names = [name]

    return [
        atom_name
        for atom_name in names
        if (resid, atom_name) in coords
    ]


# ============================================================
# 5. Evaluate every restraint in every AF3 model
# ============================================================

detail_rows = []

summary_rows = []

group_summary = defaultdict(
    lambda: {
        "total": 0,
        "evaluated": 0,
        "satisfied": 0,
        "violated": 0,
        "missing": 0,
    }
)


pdb_files = sorted(
    PDB_DIR.glob("PfMSP3pt1_sample_*_H.pdb")
)

print("\n===== FULL AF3 DISTANCE-RESTRAINT AUDIT =====")
print("AF3 models:", len(pdb_files))


for pdb in pdb_files:

    sample = int(
        re.search(
            r"sample_(\d+)_H",
            pdb.name
        ).group(1)
    )

    coords = read_coords(pdb)

    sample_satisfied = 0
    sample_violated = 0
    sample_missing = 0

    print()
    print("=" * 72)
    print(f"AF3 SAMPLE {sample}")
    print("=" * 72)

    for r in restraints:

        c1 = atom_candidates(
            coords,
            r["af3_r1"],
            r["nmr_a1"]
        )

        c2 = atom_candidates(
            coords,
            r["af3_r2"],
            r["nmr_a2"]
        )

        if not c1 or not c2:

            status = "NOT_EVALUATED"

            dmin = np.nan
            atom1 = ""
            atom2 = ""

            violation_upper = np.nan
            violation_lower = np.nan

            sample_missing += 1

        else:

            distances = []

            for a in c1:
                for b in c2:

                    d = np.linalg.norm(
                        coords[
                            (r["af3_r1"], a)
                        ] -
                        coords[
                            (r["af3_r2"], b)
                        ]
                    )

                    distances.append(
                        (d, a, b)
                    )

            distances.sort()

            dmin, atom1, atom2 = distances[0]

            violation_upper = max(
                0.0,
                dmin - r["upper"]
            )

            violation_lower = max(
                0.0,
                r["lower"] - dmin
            )

            if (
                r["lower"]
                <= dmin
                <= r["upper"]
            ):
                status = "SATISFIED"
                sample_satisfied += 1

            else:
                status = "VIOLATED"
                sample_violated += 1

        detail_rows.append({
            "AF3_sample": sample,
            "Source_line": r["source_line"],
            "NMR_residue_1": r["nmr_r1"],
            "NMR_atom_1": r["nmr_a1"],
            "NMR_residue_2": r["nmr_r2"],
            "NMR_atom_2": r["nmr_a2"],
            "AF3_residue_1": r["af3_r1"],
            "AF3_residue_2": r["af3_r2"],
            "Sequence_separation": r["separation"],
            "Restraint_class": r[
                "restraint_class"
            ],
            "Lower_bound_A": r["lower"],
            "Upper_bound_A": r["upper"],
            "Minimum_compatible_distance_A":
                dmin,
            "AF3_atom_1": atom1,
            "AF3_atom_2": atom2,
            "Upper_violation_A":
                violation_upper,
            "Lower_violation_A":
                violation_lower,
            "Status": status,
        })

        sep_label = (
            "intra"
            if r["separation"] == 0
            else f"i+{r['separation']}"
        )

        keys = [
            (
                sample,
                "all",
                "all"
            ),
            (
                sample,
                sep_label,
                "all"
            ),
            (
                sample,
                "all",
                r["restraint_class"]
            ),
            (
                sample,
                sep_label,
                r["restraint_class"]
            ),
        ]

        for key in keys:

            group_summary[key]["total"] += 1

            if status == "NOT_EVALUATED":
                group_summary[key]["missing"] += 1

            else:

                group_summary[key][
                    "evaluated"
                ] += 1

                if status == "SATISFIED":
                    group_summary[key][
                        "satisfied"
                    ] += 1

                else:
                    group_summary[key][
                        "violated"
                    ] += 1

    evaluated = (
        sample_satisfied
        + sample_violated
    )

    pct = (
        100.0
        * sample_satisfied
        / evaluated
        if evaluated
        else np.nan
    )

    summary_rows.append({
        "AF3_sample": sample,
        "Deposited_restraints":
            len(restraints),
        "Evaluated": evaluated,
        "Satisfied": sample_satisfied,
        "Violated": sample_violated,
        "Not_evaluated": sample_missing,
        "Satisfaction_percent": pct,
    })

    print(
        f"Evaluated:     {evaluated}"
    )

    print(
        f"Satisfied:     {sample_satisfied}"
    )

    print(
        f"Violated:      {sample_violated}"
    )

    print(
        f"Not evaluated: {sample_missing}"
    )

    print(
        f"Satisfaction:  {pct:.2f}%"
    )


# ============================================================
# 6. Save detailed restraint table
# ============================================================

detail_path = (
    OUT_DIR /
    "AF3_vs_all_experimental_distance_restraints.csv"
)

with detail_path.open(
    "w",
    newline=""
) as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=detail_rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(detail_rows)


# ============================================================
# 7. Save overall summary
# ============================================================

summary_path = (
    OUT_DIR /
    "AF3_all_distance_restraint_summary.csv"
)

with summary_path.open(
    "w",
    newline=""
) as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=summary_rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(summary_rows)


# ============================================================
# 8. Save stratified summary
# ============================================================

stratified_rows = []

for key, values in sorted(
    group_summary.items()
):

    sample, separation, rclass = key

    evaluated = values["evaluated"]

    pct = (
        100.0
        * values["satisfied"]
        / evaluated
        if evaluated
        else np.nan
    )

    stratified_rows.append({
        "AF3_sample": sample,
        "Sequence_group": separation,
        "Restraint_class": rclass,
        "Total": values["total"],
        "Evaluated": evaluated,
        "Satisfied": values[
            "satisfied"
        ],
        "Violated": values[
            "violated"
        ],
        "Not_evaluated": values[
            "missing"
        ],
        "Satisfaction_percent": pct,
    })


stratified_path = (
    OUT_DIR /
    "AF3_distance_restraint_stratified_summary.csv"
)

with stratified_path.open(
    "w",
    newline=""
) as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=stratified_rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(stratified_rows)


# ============================================================
# 9. Save violation-only table
# ============================================================

violations = [
    row
    for row in detail_rows
    if row["Status"] == "VIOLATED"
]

violation_path = (
    OUT_DIR /
    "AF3_distance_restraint_violations.csv"
)

with violation_path.open(
    "w",
    newline=""
) as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=detail_rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(violations)


# ============================================================
# 10. Terminal summary
# ============================================================

print()
print("===== FINAL OVERALL SUMMARY =====")

for row in summary_rows:

    print(
        f"Sample {row['AF3_sample']}: "
        f"{row['Satisfied']}/"
        f"{row['Evaluated']} satisfied "
        f"({row['Satisfaction_percent']:.2f}%), "
        f"{row['Violated']} violated, "
        f"{row['Not_evaluated']} "
        f"not evaluated"
    )


print()
print("===== MEDIUM-RANGE SUMMARY =====")

for sample in range(5):

    for separation in ["i+3", "i+4", "i+5"]:

        key = (
            sample,
            separation,
            "all"
        )

        if key not in group_summary:
            continue

        x = group_summary[key]

        pct = (
            100.0
            * x["satisfied"]
            / x["evaluated"]
            if x["evaluated"]
            else np.nan
        )

        print(
            f"Sample {sample} "
            f"{separation:4s}: "
            f"{x['satisfied']}/"
            f"{x['evaluated']} "
            f"satisfied "
            f"({pct:.2f}%)"
        )


print()
print("===== FILES SAVED =====")

for path in [
    detail_path,
    summary_path,
    stratified_path,
    violation_path,
]:
    print(path)

