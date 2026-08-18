# Reproducibility

This directory provides project-level reproducibility and provenance guidance for the PfMSP3.1 SPAM structural-characterisation repository.

The repository contains both historical computational work originating from the 2020 Master's project and further investigation performed in 2026. These should be interpreted separately.

## Historical 2020 work

Historical material has been reorganised by scientific workflow:

- structural modelling: `../02_structural_modelling/`
- molecular-dynamics simulations: `../05_MD_simulations/`
- MD analysis: `../06_MD_analysis/original_2020/`
- protein-protein docking: `../07_protein_docking/historical_2020/`
- complex MD: `../08_complex_MD/historical_2020/`
- thesis figures: `../09_figures/historical_2020/`
- reconstructed thesis tables: `../10_tables/historical_2020/`

The historical files are preserved as surviving evidence of the original workflow. Not every original command or software environment from 2020 could be reconstructed.

## Reconstructed historical results

Some thesis result tables were reconstructed in 2026 using the final thesis together with surviving computational outputs.

These are stored under:

`../10_tables/historical_2020/`

The accompanying README documents their provenance and interpretation.

## AlphaFold-related investigation in 2026

The AlphaFoldDB entry A0A8G1DNL0 was investigated during the 2026 further work.

Subsequent sequence comparison showed that A0A8G1DNL0 contains 121 amino acids and does not sequence-match the historical 139-aa SPAM modelling sequence.

Therefore, the A0A8G1DNL0-derived analyses should not be interpreted as direct structural validation of the historical SPAM model.

See:

`../03_AlphaFold_validation/README.md`

## 2026 molecular-dynamics simulation

The A0A8G1DNL0-derived model was subjected to a 250-ns MD investigation.

Simulation setup and execution records are documented in:

`../05_MD_simulations/further_investigation_2026/AlphaFold_model/README.md`

Key verified production parameters include:

- GROMACS 2020.7 for HPC production execution
- GROMACS 2026.0 for system/topology preparation
- CHARMM36 July 2022 force field
- SPC water option during topology preparation
- 2-fs timestep
- 125,000,000 production steps
- 250-ns intended production duration
- 300 K temperature
- 1 bar pressure
- V-rescale temperature coupling
- Parrinello-Rahman pressure coupling
- PME electrostatics
- 1.2-nm Coulomb and van der Waals cutoffs
- LINCS constraints

## 2026 MD analysis

Downstream analysis of the A0A8G1DNL0-derived trajectory is documented in:

`../06_MD_analysis/further_investigation_2026/AlphaFold_model/README.md`

Analysis categories include RMSD, RMSF, radius of gyration, hydrogen bonds, SASA, PCA, clustering, helix distances and secondary structure.

## Large generated files

Some MD-analysis outputs are too large for standard GitHub storage.

The clustering matrix:

`../06_MD_analysis/further_investigation_2026/AlphaFold_model/clustering/clusters_FINAL_080.xpm`

is approximately 597 MB and is intentionally excluded from Git tracking through `.gitignore`.

Smaller supporting outputs and clustering logs are retained in the repository.

## Reproducibility principle

The repository aims to distinguish clearly between:

- original historical files;
- reconstructed historical results;
- further investigation performed in 2026; and
- future work not yet completed.

Files should not be interpreted as newly reproduced historical results unless this is explicitly stated in their accompanying documentation.
