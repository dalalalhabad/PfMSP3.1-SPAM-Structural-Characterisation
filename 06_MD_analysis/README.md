# Molecular-dynamics analysis

This directory contains molecular-dynamics analysis material from the PfMSP3.1 SPAM structural-characterisation project.

The contents are separated into:

1. historical analysis recovered from the 2020 Master's project; and
2. further analysis performed in 2026.

## Historical 2020 analysis

Historical analysis files are stored under:

`original_2020/`

### RMSD data

`original_2020/RMSD_data/`

Contains numerical RMSD-related data recovered from the original 2020 project for all three MD replicates.

For each replicate, two historical datasets are preserved:

- `frame0`
- `frame5001`

These filenames reflect the names used in the original project files. They are preserved as historical numerical analysis data and should not be reinterpreted beyond what is supported by the original workflow.

The associated historical plotting-configuration file `RMSD.m2p.txt` was not copied because it contained xpm2ps/PostScript formatting settings rather than RMSD measurements.

### Equilibration analysis

`original_2020/equilibration_analysis/`

Contains historical GROMACS analysis outputs:

- `density.xvg`
- `potential.xvg`
- `pressure.xvg`
- `temperature.xvg`

These files correspond to equilibration/system-condition analyses from the historical MD workflow.

### Salt-bridge distances

`original_2020/salt_bridge_distances/`

Contains residue-pair distance data for salt-bridge interactions monitored across the three historical MD replicates.

Separate directories are retained for:

- `replicate_1/`
- `replicate_2/`
- `replicate_3/`

These files provide the underlying numerical data associated with the salt-bridge analyses reported in the thesis.

### Structural snapshots

`original_2020/structural_snapshots/`

Contains one recovered non-empty structural PDB file for each historical MD replicate:

- `replicate_1_structure.pdb`
- `replicate_2_structure.pdb`
- `replicate_3_structure.pdb`

These structures were recovered from the original 2020 project directory.

Earlier zero-byte placeholder files labelled as first/last frames were removed during repository reconstruction because they did not contain structural data.

The surviving PDB files are therefore described conservatively as recovered replicate structures rather than being assigned an unsupported first-frame or last-frame interpretation.

## Further investigation — 2026

`further_investigation_2026/AlphaFold_model/`

Contains analysis performed in 2026 on the A0A8G1DNL0-derived AlphaFoldDB model.

Analysis categories include:

- RMSD
- RMSF
- radius of gyration
- hydrogen-bond analysis
- solvent-accessible surface area
- principal component analysis
- clustering
- helix-distance analysis
- secondary-structure analysis

Detailed provenance and interpretation are documented in:

`further_investigation_2026/AlphaFold_model/README.md`

## Important provenance note

The 2026 A0A8G1DNL0-derived model contains 121 amino acids and does not sequence-match the historical 139-aa PfMSP3.1 SPAM model.

Therefore, the 2026 analysis should not be interpreted as direct validation of the historical SPAM structural model.

The historical 2020 analysis and the 2026 further investigation are retained separately to avoid conflating the two workflows.

## Large generated files

Some analysis outputs are too large for normal GitHub storage.

The 2026 clustering matrix:

`further_investigation_2026/AlphaFold_model/clustering/clusters_FINAL_080.xpm`

is approximately 597 MB and is intentionally excluded from Git tracking through `.gitignore`.

Historical large trajectory files are likewise retained outside the repository.

## Provenance

Historical files were recovered from the original 2020 Master's project and reorganised in 2026.

The repository preserves surviving numerical and structural analysis data while avoiding unsupported reconstruction of missing historical outputs.
