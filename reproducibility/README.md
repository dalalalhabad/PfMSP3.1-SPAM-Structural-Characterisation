# Reproducibility and provenance

This directory provides project-level reproducibility and provenance
guidance for the PfMSP3.1 SPAM structural-characterisation repository.

The repository contains computational work from two distinct periods:

1. the original 2020 Master's research project; and
2. further structural investigation and reassessment performed in 2026.

These two periods are intentionally distinguished throughout the
repository.

## Historical 2020 work

Historical material has been reorganised by scientific workflow:

- original sequence-analysis material:
  `../01_original_2020_work/`
- structural modelling:
  `../02_structural_modelling/`
- molecular-dynamics simulations:
  `../05_MD_simulations/`
- molecular-dynamics analysis:
  `../06_MD_analysis/original_2020/`
- protein–protein docking:
  `../07_protein_docking/historical_2020/`
- protein-complex molecular dynamics:
  `../08_complex_MD/historical_2020/`
- historical thesis figures:
  `../09_figures/historical_2020/`
- reconstructed historical thesis tables:
  `../10_tables/historical_2020/`

The historical files are preserved as surviving evidence of the original
computational workflow.

Not every command, intermediate file or software environment from 2020
could be reconstructed. Missing historical material has not been
invented or replaced with inferred data.

## Reconstructed historical results

Some historical thesis result tables were reconstructed in 2026 using
the final Master's thesis together with surviving computational outputs.

These are stored under:

`../10_tables/historical_2020/`

The accompanying README documents their provenance and interpretation.

Reconstructed tables should not be confused with newly rerun historical
analyses.

## Exploratory AlphaFold investigation — 2026

The AlphaFold Database entry A0A8G1DNL0 was investigated during the
initial 2026 reassessment.

Sequence comparison subsequently established that A0A8G1DNL0 contains
121 amino acids and does not sequence-match the historical 139-aa
PfMSP3.1 SPAM modelling construct.

Accordingly, analyses based on A0A8G1DNL0 are retained as exploratory
work and should not be interpreted as direct structural validation or
rejection of the historical 139-aa SPAM model.

The sequence-provenance investigation is documented under:

`../03_exploratory_AlphaFold_comparison/`

## Exploratory 2026 molecular-dynamics simulation

The A0A8G1DNL0-derived model was subjected to a 250-ns
molecular-dynamics investigation before the sequence mismatch was fully
resolved.

Simulation setup and execution records are documented in:

`../05_MD_simulations/further_investigation_2026/AlphaFold_model/README.md`

Verified production and preparation records include:

- GROMACS 2026.0 for system and topology preparation;
- GROMACS 2020.7 for HPC production execution;
- CHARMM36 July 2022 force field;
- SPC water option during topology preparation;
- 2-fs timestep;
- 125,000,000 production steps;
- 250-ns intended production duration;
- 300 K reference temperature;
- 1 bar reference pressure;
- V-rescale temperature coupling;
- Parrinello-Rahman pressure coupling;
- PME electrostatics;
- 1.2-nm Coulomb and van der Waals cutoffs; and
- LINCS constraints.

Because the underlying A0A8G1DNL0 sequence is not sequence-matched to the
historical construct, this simulation is retained as exploratory
provenance rather than direct validation of the historical model.

## Exploratory 2026 MD analysis

Downstream analysis of the A0A8G1DNL0-derived trajectory is documented
under:

`../06_MD_analysis/further_investigation_2026/AlphaFold_model/`

Analysis categories include:

- RMSD;
- RMSF;
- radius of gyration;
- hydrogen bonds;
- solvent-accessible surface area;
- principal component analysis;
- clustering;
- helix-distance analysis; and
- secondary-structure analysis.

These analyses should be interpreted together with the sequence-mismatch
caveat described above.

## Sequence-matched AF3/NMR reassessment — 2026

Following identification of the A0A8G1DNL0 sequence mismatch, a separate
sequence-matched reassessment was undertaken using AlphaFold 3
predictions generated from the exact historical 139-aa SPAM sequence.

This reassessment is documented under:

`../04_AF3_vs_experimental_NMR/`

The sequence-matched AF3 models were supplied by Prof. Brian Smith.

The original externally supplied AF3 prediction package is retained
outside the public Git repository and is not redistributed here.

The public repository preserves:

- AF3-input provenance documentation;
- the historical MODELLER structure;
- the deposited experimental NMR restraint file;
- restraint-analysis scripts;
- derived AF3 restraint-evaluation results;
- historical-model restraint evaluation;
- structural-alignment results; and
- the final scientific interpretation.

The AF3 models were evaluated directly against the experimental NMR
restraints associated with the SPAM-H1 region.

The deposited 1PSM coordinate ensemble was not treated as the sole or
primary experimental benchmark because those coordinates themselves
represent a structural interpretation of the underlying NMR data.

## AF3/NMR reproducibility notes

The experimental restraint file used in the reassessment is retained at:

`../04_AF3_vs_experimental_NMR/input/NMR_experimental_data/1PSM.mr`

The historical structural model evaluated against the same evidence is:

`../04_AF3_vs_experimental_NMR/input/historical_model/model.B99990034_original.pdb`

Analysis scripts are retained under:

`../04_AF3_vs_experimental_NMR/scripts/`

Derived results are retained under:

`../04_AF3_vs_experimental_NMR/results/`

The exact software build used to generate the externally supplied AF3
predictions was not independently recorded in this repository and is
therefore not inferred.

Similarly, software-version information that cannot be verified from
surviving records is not reconstructed retrospectively.

## 2026 reassessment figures

Figures generated during the modern reassessment are separated from the
historical thesis figures.

They are stored under:

`../09_figures/reassessment_2026/`

Historical figures remain under:

`../09_figures/historical_2020/`

This separation prevents modern analytical figures from being
misidentified as material originating from the 2020 Master's project.

## Large generated files

Some molecular-dynamics outputs are unsuitable for standard Git
distribution because of their size.

For example, the generated clustering matrix:

`../06_MD_analysis/further_investigation_2026/AlphaFold_model/clustering/clusters_FINAL_080.xpm`

is approximately 597 MB and is intentionally excluded from Git tracking.

Complete MD trajectory files and other large trajectory-derived binary
files may also be retained outside the public repository.

Smaller analytical outputs, logs, structures and parameter files are
retained where practical.

## External and third-party material

Public availability of this repository does not imply that externally
supplied or third-party material has been relicensed.

Original externally supplied AF3 prediction files are not redistributed.

Where third-party experimental or structural data are retained for
reproducibility, their original provenance should be respected and the
relevant original data sources should be cited where applicable.

## Reproducibility principle

The repository aims to distinguish clearly between:

- original historical 2020 files;
- historical results reconstructed from surviving records;
- exploratory 2026 analyses;
- sequence-matched 2026 reassessment analyses;
- externally supplied source material;
- derived analytical outputs; and
- large or externally supplied files retained outside public Git.

Files should not be interpreted as newly reproduced historical results
unless this is explicitly stated in their accompanying documentation.

Where exact provenance, software versions or historical execution details
cannot be verified, the repository documents that limitation rather than
inferring missing information.