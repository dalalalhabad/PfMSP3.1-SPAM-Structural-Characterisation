# Molecular-dynamics simulations

This directory contains molecular-dynamics simulation material associated with the PfMSP3.1 SPAM project.

The contents are divided into:

1. the historical 2020 MD workflow performed on the selected MODELLER SPAM structure; and
2. further MD investigation performed in 2026 on the A0A8G1DNL0-derived AlphaFoldDB model.

## Historical 2020 SPAM MD workflow

The historical simulation workflow is organised into:

### System setup

`system_setup/`

Contains the selected MODELLER structure and the prepared GROMACS system, including processed, boxed, solvated and ionised structures.

### Topology

`topology/`

Contains the retained topology and position-restraint files used for the historical SPAM simulation.

### Parameters

`parameters/`

Contains the historical minimisation, ion, NVT and NPT parameter files.

The subdirectory:

`parameters/historical_10ns_test/`

contains an earlier 10-ns production-test parameter file retained for provenance.

### Equilibration

`equilibration/`

Contains structural outputs and supporting records from energy minimisation, NVT equilibration and NPT equilibration.

Subdirectories include:

- `energy_minimisation/`
- `NVT/`
- `NPT/`

The retained files include logs, energy files, TPR files and final checkpoints where available.

Large equilibration trajectories were intentionally not copied into the Git repository.

### Production MD

`production/`

Contains three independent historical production replicates:

- `replicate_1/`
- `replicate_2/`
- `replicate_3/`

Each replicate retains its production parameter file, TPR file and command file.

Large historical trajectory files are not included in the repository because they exceed normal GitHub storage limits.

## 2026 further investigation

`further_investigation_2026/AlphaFold_model/`

Contains the setup and execution records for a 250-ns simulation performed on the A0A8G1DNL0-derived AlphaFoldDB model.

This model contains 121 amino acids and does not sequence-match the historical 139-aa SPAM modelling sequence.

Therefore, the 2026 simulation should not be interpreted as direct validation of the historical SPAM structural model.

Detailed simulation parameters and provenance are documented in:

`further_investigation_2026/AlphaFold_model/README.md`

## Analysis outputs

Historical and 2026 analysis outputs are stored separately under:

`../06_MD_analysis/`

This separation keeps simulation setup/execution files distinct from downstream structural analyses.

## Provenance

The historical files were recovered from the original 2020 Master's project and reorganised into this repository in 2026.

Large trajectories and other oversized generated files were intentionally excluded, while key setup, parameter, topology, log, checkpoint and production-control files were retained to preserve the computational workflow.
