from pathlib import Path
import re
import csv
import numpy as np
from openmm import app, unit

ROOT = Path("04_AF3_vs_experimental_NMR")

HIST = (
    ROOT /
    "input/historical_model/"
    "model.B99990034_original.pdb"
)

AF3_DIR = (
    ROOT /
    "input/AF3_model/"
    "PfMSP3pt1-2774654e-f422-44c5-9c56-f562b85e2029/"
    "PfMSP3pt1/seed_40920/predictions"
)

RESULTS = ROOT / "results"
RESULTS.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# Coordinate reader
# ------------------------------------------------------------

def read_structure(path):

    if path.suffix.lower() == ".cif":
        structure = app.PDBxFile(str(path))
    else:
        structure = app.PDBFile(str(path))

    coords = {}
    residue_names = {}

    for atom in structure.topology.atoms():

        resid = int(atom.residue.id)
        atom_name = atom.name.upper()

        xyz = structure.positions[
            atom.index
        ].value_in_unit(unit.angstrom)

        coords[(resid, atom_name)] = np.asarray(
            xyz,
            dtype=float
        )

        residue_names[resid] = atom.residue.name

    return coords, residue_names


# ------------------------------------------------------------
# Kabsch superposition
# ------------------------------------------------------------

def kabsch_fit(mobile, reference):

    mobile = np.asarray(mobile, dtype=float)
    reference = np.asarray(reference, dtype=float)

    mob_centroid = mobile.mean(axis=0)
    ref_centroid = reference.mean(axis=0)

    mob0 = mobile - mob_centroid
    ref0 = reference - ref_centroid

    H = mob0.T @ ref0

    U, S, Vt = np.linalg.svd(H)

    R = Vt.T @ U.T

    if np.linalg.det(R) < 0:
        Vt[-1, :] *= -1
        R = Vt.T @ U.T

    fitted = (
        (mobile - mob_centroid) @ R.T
        + ref_centroid
    )

    return fitted


def rmsd(a, b):

    a = np.asarray(a)
    b = np.asarray(b)

    return np.sqrt(
        np.mean(
            np.sum(
                (a-b)**2,
                axis=1
            )
        )
    )


# ------------------------------------------------------------
# Regions
# ------------------------------------------------------------

regions = [
    (
        "Full_139aa",
        1,
        139
    ),
    (
        "Experimental_SPAM_H1_7_44",
        7,
        44
    ),
    (
        "Experimental_helical_region_16_41",
        16,
        41
    ),
    (
        "C_terminal_NMR_region_37_44",
        37,
        44
    ),
]

hist_coords, hist_resnames = read_structure(HIST)

summary_rows = []
per_residue_rows = []

af3_files = sorted(
    AF3_DIR.glob("PfMSP3pt1_sample_*.cif")
)

print("===== HISTORICAL MODEL vs AF3 STRUCTURAL ALIGNMENT =====")
print("Historical model:", HIST)
print("AF3 models:", len(af3_files))


for af3_file in af3_files:

    sample = int(
        re.search(
            r"sample_(\d+)",
            af3_file.name
        ).group(1)
    )

    af3_coords, af3_resnames = read_structure(
        af3_file
    )

    print()
    print("=" * 76)
    print(f"AF3 SAMPLE {sample}")
    print("=" * 76)

    # --------------------------------------------------------
    # Regional RMSDs
    # --------------------------------------------------------

    for label, start, end in regions:

        # CA
        hist_ca = []
        af3_ca = []

        for resid in range(start, end+1):

            hk = (resid, "CA")
            ak = (resid, "CA")

            if hk in hist_coords and ak in af3_coords:
                hist_ca.append(hist_coords[hk])
                af3_ca.append(af3_coords[ak])

        hist_ca = np.vstack(hist_ca)
        af3_ca = np.vstack(af3_ca)

        fitted_ca = kabsch_fit(
            af3_ca,
            hist_ca
        )

        ca_rmsd = rmsd(
            fitted_ca,
            hist_ca
        )

        # Backbone N/CA/C
        hist_bb = []
        af3_bb = []

        for resid in range(start, end+1):

            for atom in ["N", "CA", "C"]:

                hk = (resid, atom)
                ak = (resid, atom)

                if hk in hist_coords and ak in af3_coords:
                    hist_bb.append(hist_coords[hk])
                    af3_bb.append(af3_coords[ak])

        hist_bb = np.vstack(hist_bb)
        af3_bb = np.vstack(af3_bb)

        fitted_bb = kabsch_fit(
            af3_bb,
            hist_bb
        )

        bb_rmsd = rmsd(
            fitted_bb,
            hist_bb
        )

        summary_rows.append({
            "AF3_sample": sample,
            "Region": label,
            "Residue_start": start,
            "Residue_end": end,
            "Residues_compared": len(hist_ca),
            "CA_RMSD_A": ca_rmsd,
            "Backbone_N_CA_C_RMSD_A": bb_rmsd,
        })

        print(
            f"{label:36s} "
            f"CA={ca_rmsd:7.3f} Å   "
            f"backbone={bb_rmsd:7.3f} Å"
        )

    # --------------------------------------------------------
    # Per-residue CA displacement after alignment on
    # the complete experimental SPAM-H1 region 7–44.
    # --------------------------------------------------------

    start = 7
    end = 44

    hist_region = np.vstack([
        hist_coords[(r, "CA")]
        for r in range(start, end+1)
    ])

    af3_region = np.vstack([
        af3_coords[(r, "CA")]
        for r in range(start, end+1)
    ])

    fitted_region = kabsch_fit(
        af3_region,
        hist_region
    )

    for idx, resid in enumerate(
        range(start, end+1)
    ):

        deviation = np.linalg.norm(
            fitted_region[idx] -
            hist_region[idx]
        )

        # Corresponding experimental NMR numbering.
        nmr_resid = resid - 6

        per_residue_rows.append({
            "AF3_sample": sample,
            "Historical_AF3_residue": resid,
            "NMR_residue": nmr_resid,
            "Residue_name":
                hist_resnames[resid],
            "CA_displacement_A":
                deviation,
        })


# ------------------------------------------------------------
# Save structural summary
# ------------------------------------------------------------

summary_path = (
    RESULTS /
    "Historical_vs_AF3_structural_RMSD_summary.csv"
)

with summary_path.open("w", newline="") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=summary_rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(summary_rows)


# ------------------------------------------------------------
# Save per-residue deviations
# ------------------------------------------------------------

per_residue_path = (
    RESULTS /
    "Historical_vs_AF3_SPAM_H1_per_residue_CA_deviation.csv"
)

with per_residue_path.open("w", newline="") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=per_residue_rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(per_residue_rows)


# ------------------------------------------------------------
# Highlight experimentally interesting residues
# ------------------------------------------------------------

interesting_nmr = {
    14,
    19,
    22,
    31,
    36,
    37,
    38,
}

print()
print("===== PER-RESIDUE CA DEVIATIONS AT KEY NMR POSITIONS =====")

for sample in range(5):

    print()
    print(f"AF3 sample {sample}")

    selected = [
        r for r in per_residue_rows
        if r["AF3_sample"] == sample
        and r["NMR_residue"] in interesting_nmr
    ]

    for r in selected:

        print(
            f"NMR {r['NMR_residue']:2d} / "
            f"construct {r['Historical_AF3_residue']:2d} "
            f"{r['Residue_name']:3s}: "
            f"{r['CA_displacement_A']:.3f} Å"
        )


print()
print("===== FILES SAVED =====")
print(summary_path)
print(per_residue_path)

