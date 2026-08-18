# PfMSP3.1 SPAM Structural Characterisation

Computational structural and functional characterisation of the SPAM domain of *Plasmodium falciparum* merozoite surface protein 3.1 (PfMSP3.1).

This repository preserves and organises computational work originating from a 2020 Master's research project and documents further structural investigations undertaken in 2026. It contains sequence-analysis material, structural modelling, molecular-dynamics simulations and analyses, protein-protein docking, complex MD analyses, historical thesis figures and reconstructed thesis result tables.

## Project history

### Original study — 2020

The original project investigated the structural characteristics of the PfMSP3.1 SPAM domain using computational approaches including:

- sequence and coiled-coil analysis;
- CCBuilder-assisted structural modelling;
- MODELLER comparative modelling;
- structural model assessment;
- molecular-dynamics simulation of the SPAM model;
- analysis of structural stability and salt-bridge interactions;
- protein-protein docking against C1 inhibitor (C1-INH) structures;
- ZRANK rescoring of docked complexes;
- buried surface area analysis; and
- molecular-dynamics analysis of selected protein complexes.

Historical files recovered from the original project have been reorganised into a clearer repository structure while retaining their relationship to the 2020 Master's thesis.

### Further investigation — 2026

The project was revisited in 2026 to preserve the original computational work, improve reproducibility, and investigate the historical structural model using newer structural information and computational approaches.

The repository therefore distinguishes between:

1. historical work originating from the 2020 project;
2. reconstructed or reorganised historical results;
3. further analyses performed in 2026; and
4. planned validation or publication-related work.

## Repository structure

- `01_original_2020_work/` — preserved original 2020 material that does not belong more naturally within the reconstructed workflow, currently including sequence-analysis material and documentation.

- `02_structural_modelling/` — structural modelling material, including CCBuilder and MODELLER files.

- `03_AlphaFold_validation/` — AlphaFold-related material examined during the 2026 further investigation. The investigated AlphaFoldDB entry A0A8G1DNL0 contains 121 residues and does not sequence-match the historical 139-aa SPAM model; it is therefore retained as an investigated reference rather than direct structural validation. A sequence-matched modern prediction remains future work.

- `04_cryoEM_validation/` — reserved for planned cryo-EM structural comparison/validation work; currently no analysis files are included.

- `05_MD_simulations/` — molecular-dynamics simulation setup and simulation material, including historical/reconstructed work and further investigation performed in 2026.

- `06_MD_analysis/` — molecular-dynamics analysis material. Historical 2020 files include structural snapshots and salt-bridge distance data; further 2026 analyses include additional structural and trajectory analyses.

- `07_protein_docking/` — reconstructed historical protein-protein docking material, including docking structures, ZRANK-related results and surface-area analysis.

- `08_complex_MD/` — historical molecular-dynamics material for selected docked complexes and post-MD structural comparison.

- `09_figures/` — recovered historical thesis figures. The original thesis figures are stored under `09_figures/historical_2020/thesis_figures/`.

- `10_tables/` — reconstructed numerical tables reported in the 2020 thesis, including MODELLER scoring, ZRANK rankings and ZRANK/BSA comparison before and after MD.

- `11_supplementary/` — reserved for supplementary material if required for a future manuscript. The final 2020 thesis did not contain a formal supplementary or appendix section.

- `docs/` — repository documentation and inventories.

- `manuscript/` — reserved for manuscript-related material.

- `reproducibility/` — reserved for consolidated reproducibility documentation, including commands, software versions and workflow information.

## Historical thesis tables

Reconstructed thesis tables are stored in:

`10_tables/historical_2020/`

These currently include:

- `Table_4_MODELLER_objective_function_DOPE.csv`
- `Table_5_ZRANK_top20_complexes.csv`
- `Table_6_ZRANK_BSA_before_after_MD.csv`

These files preserve values reported in the historical thesis and should be interpreted in the context of the original 2020 workflow. Further details are provided in `10_tables/historical_2020/README.md`.

## Historical thesis figures

Recovered figures from the Master's thesis are stored in:

`09_figures/historical_2020/thesis_figures/`

An inventory and description of the recovered figures is maintained in:

`docs/figure_inventory.md`

The historical figures are preserved separately from figures that may later be generated from the 2026 further investigation.

## Large generated files

Some computational analyses generate files that are unsuitable for normal GitHub storage because of their size. Large intermediate/generated files may therefore be retained locally and excluded through `.gitignore`.

For example, the large clustering matrix generated during the 2026 AlphaFold-model MD analysis is intentionally excluded from Git tracking.

## Reproducibility and provenance

The repository is being organised so that historical results are not silently presented as newly generated results.

Where possible, files are identified according to their provenance as:

- original 2020 material;
- reconstructed/reorganised historical material; or
- further investigation performed in 2026.

This distinction is particularly important where historical thesis tables have been reconstructed from the final thesis and surviving computational outputs.

## Status

This repository is under active development.

The historical 2020 Master's research material is being preserved and documented, while additional structural analyses are being investigated in preparation for potential publication. Planned analyses should not be interpreted as completed results unless corresponding files and documentation are present in the repository.
