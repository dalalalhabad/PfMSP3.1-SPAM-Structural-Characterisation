from pathlib import Path
import csv
from collections import defaultdict
import statistics

ROOT = Path("04_AF3_vs_experimental_NMR")
RESULTS = ROOT / "results"

src = RESULTS / "AF3_distance_restraint_violations.csv"

rows = list(csv.DictReader(src.open()))

print("===== AF3 CONSENSUS VIOLATION AUDIT =====")
print("Violation records across all models:", len(rows))

groups = defaultdict(list)

for r in rows:
    key = (
        r["Source_line"],
        r["NMR_residue_1"],
        r["NMR_atom_1"],
        r["NMR_residue_2"],
        r["NMR_atom_2"],
        r["Sequence_separation"],
        r["Restraint_class"],
        r["Upper_bound_A"],
    )
    groups[key].append(r)

summary = []

for key, vals in groups.items():

    samples = sorted(
        int(v["AF3_sample"])
        for v in vals
    )

    violations = [
        float(v["Upper_violation_A"])
        for v in vals
        if v["Upper_violation_A"] not in ("", "nan")
    ]

    distances = [
        float(v["Minimum_compatible_distance_A"])
        for v in vals
        if v["Minimum_compatible_distance_A"] not in ("", "nan")
    ]

    (
        source_line,
        r1,
        a1,
        r2,
        a2,
        separation,
        rclass,
        upper,
    ) = key

    summary.append({
        "Source_line": source_line,
        "NMR_residue_1": r1,
        "NMR_atom_1": a1,
        "NMR_residue_2": r2,
        "NMR_atom_2": a2,
        "Sequence_separation": separation,
        "Restraint_class": rclass,
        "Upper_bound_A": upper,
        "Models_violated": len(vals),
        "Samples_violated": ",".join(map(str, samples)),
        "Mean_distance_A": statistics.mean(distances),
        "Mean_upper_violation_A": statistics.mean(violations),
        "Minimum_upper_violation_A": min(violations),
        "Maximum_upper_violation_A": max(violations),
    })

summary.sort(
    key=lambda r: (
        -int(r["Models_violated"]),
        -float(r["Mean_upper_violation_A"])
    )
)

out = RESULTS / "AF3_consensus_violation_summary.csv"

with out.open("w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=summary[0].keys()
    )
    writer.writeheader()
    writer.writerows(summary)

print("\n===== NUMBER OF UNIQUE RESTRAINTS VIOLATED =====")
print("Unique restraints:", len(summary))

for n in range(5, 0, -1):
    x = [r for r in summary if int(r["Models_violated"]) == n]
    print(f"Violated in {n}/5 models: {len(x)}")

print("\n===== CONSENSUS 5/5 VIOLATIONS =====")

consensus = [
    r for r in summary
    if int(r["Models_violated"]) == 5
]

for i, r in enumerate(consensus, 1):

    sep = int(r["Sequence_separation"])

    label = (
        "intra"
        if sep == 0
        else f"i→i+{sep}"
    )

    print()
    print(
        f"{i}. NMR {r['NMR_residue_1']} {r['NMR_atom_1']} "
        f"↔ {r['NMR_residue_2']} {r['NMR_atom_2']}"
    )

    print(
        f"   class: {r['Restraint_class']} | "
        f"{label}"
    )

    print(
        f"   experimental upper bound: "
        f"{float(r['Upper_bound_A']):.2f} Å"
    )

    print(
        f"   mean AF3 distance: "
        f"{float(r['Mean_distance_A']):.3f} Å"
    )

    print(
        f"   mean violation: "
        f"{float(r['Mean_upper_violation_A']):.3f} Å"
    )

    print(
        f"   violation range: "
        f"{float(r['Minimum_upper_violation_A']):.3f}–"
        f"{float(r['Maximum_upper_violation_A']):.3f} Å"
    )

print("\n===== 5/5 DIRECT-UNAMBIGUOUS VIOLATIONS =====")

direct = [
    r for r in consensus
    if r["Restraint_class"] == "direct_unambiguous"
]

print("Number:", len(direct))

for r in direct:

    print(
        f"NMR {r['NMR_residue_1']} {r['NMR_atom_1']} "
        f"↔ {r['NMR_residue_2']} {r['NMR_atom_2']} | "
        f"sep={r['Sequence_separation']} | "
        f"upper={float(r['Upper_bound_A']):.2f} Å | "
        f"mean distance={float(r['Mean_distance_A']):.3f} Å | "
        f"mean violation={float(r['Mean_upper_violation_A']):.3f} Å"
    )

print("\n===== 5/5 MEDIUM-RANGE VIOLATIONS =====")

medium = [
    r for r in consensus
    if int(r["Sequence_separation"]) >= 3
]

print("Number:", len(medium))

for r in medium:
    print(
        f"NMR {r['NMR_residue_1']} {r['NMR_atom_1']} "
        f"↔ {r['NMR_residue_2']} {r['NMR_atom_2']} | "
        f"i→i+{r['Sequence_separation']} | "
        f"class={r['Restraint_class']} | "
        f"upper={float(r['Upper_bound_A']):.2f} Å | "
        f"mean violation={float(r['Mean_upper_violation_A']):.3f} Å"
    )

print("\nSaved:")
print(out)

