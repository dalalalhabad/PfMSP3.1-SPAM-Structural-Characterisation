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
4. exploratory and reassessment analyses undertaken in 2026.

## Repository structure

- `01_original_2020_work/` — preserved original 2020 material that does not belong more naturally within the reconstructed workflow, currently including sequence-analysis material and documentation.

- `02_structural_modelling/` — structural modelling material, including CCBuilder and MODELLER files.

- `03_exploratory_AlphaFold_comparison/` — earlier AlphaFold-related material examined during the 2026 further investigation. The investigated AlphaFoldDB entry A0A8G1DNL0 contains 121 residues and does not sequence-match the historical 139-aa SPAM model; it is therefore retained as an investigated reference rather than direct structural validation.

- `04_AF3_vs_experimental_NMR/` — completed 2026 reassessment of sequence-matched AlphaFold 3 (AF3) predictions against the original experimental NMR evidence for SPAM-H1. This branch contains provenance documentation for the sequence-matched AF3 predictions, experimental NMR restraint data, the preserved historical model, analysis scripts, derived restraint-evaluation results and final interpretation. The original externally supplied AF3 prediction package is retained outside the public Git repository.

- `05_MD_simulations/` — molecular-dynamics simulation setup and simulation material, including historical/reconstructed work and further investigation performed in 2026.

- `06_MD_analysis/` — molecular-dynamics analysis material. Historical 2020 files include structural snapshots and salt-bridge distance data; further 2026 analyses include additional structural and trajectory analyses.

- `07_protein_docking/` — reconstructed historical protein-protein docking material, including docking structures, ZRANK-related results and surface-area analysis.

- `08_complex_MD/` — historical molecular-dynamics material for selected docked complexes and post-MD structural comparison.

- `09_figures/` — figures associated with both the historical 2020 project and the 2026 structural reassessment. Historical thesis figures are stored under `09_figures/historical_2020/thesis_figures/`, while figures generated during the sequence-matched 2026 reassessment are stored under `09_figures/reassessment_2026/`.

- `10_tables/` — reconstructed numerical tables reported in the 2020 thesis, including MODELLER scoring, ZRANK rankings and ZRANK/BSA comparison before and after MD.

- `docs/` — repository documentation and inventories.

- `reproducibility/` — project-level provenance and reproducibility documentation linking the historical 2020 workflow, reconstructed thesis results and verified 2026 simulation/analysis settings.

## Historical thesis tables

Reconstructed numerical tables reported in the 2020 thesis are stored in:

`10_tables/historical_2020/`

These include:

- `Table_4_MODELLER_objective_function_DOPE.csv` — MODELLER objective-function and DOPE scores for the ten models reported in thesis Table 4. These ten models were selected by objective-function ranking; the accompanying DOPE values describe that selected set and should not be interpreted as a global DOPE ranking of all 100 generated MODELLER models.
- `Table_5_ZRANK_top20_complexes.csv` — the top 20 protein-protein docking complexes reported according to ZRANK score.
- `Table_6_ZRANK_BSA_before_after_MD.csv` — the reported comparison of ZRANK scores and buried surface area (BSA) before and after MD for the selected complexes.

These tables were reconstructed in 2026 from the final thesis together with surviving historical computational outputs. They preserve the numerical results reported in the thesis rather than representing newly rerun analyses.

Detailed provenance and interpretation are documented in:

`10_tables/historical_2020/README.md`

## Historical surface-area workbooks

Historical buried-surface-area analysis workbooks are retained under:

`07_protein_docking/historical_2020/surface_area_analysis/`

The surviving files include:

- `1_Surface_area.xlsx` — contains three historical analysis worksheets;
- `2_Surface_area.xlsx` — contains one historical analysis worksheet; and
- `3_Surface_area.xlsx` — contains one historical analysis worksheet.

Although the worksheet dimensions of the latter two correspond broadly to worksheets within `1_Surface_area.xlsx`, direct cell-by-cell comparison confirmed that they are not identical copies. They are therefore preserved as separate historical analysis files rather than treated as duplicates.

## Historical thesis figures

Recovered figures from the Master's thesis are stored in:

`09_figures/historical_2020/thesis_figures/`

An inventory and description of the recovered figures is maintained in:

`docs/figure_inventory.md`

The historical figures are preserved separately from figures generated during the 2026 structural reassessment, which are stored under `09_figures/reassessment_2026/`.

## Raw MD data and large generated files

The public project is organised in two complementary layers.

**GitHub serves as the readable and reproducible scientific record.** It contains the retained structures, simulation parameter files, topology and restraint files, TPR run inputs where appropriate, logs, scripts and command records, selected structural outputs, derived analysis data, docking results, figures and reconstructed thesis tables.

**Full-resolution raw MD data are maintained separately.** Large trajectory and generated files are not stored directly in the Git repository because of normal repository file-size constraints. These files are not considered missing from the underlying project data; they are retained outside Git as raw simulation data.

For the historical MD work, large trajectory files such as full-resolution `.xtc` and `.trr` outputs are therefore excluded from the Git repository, while the surviving simulation inputs, parameters, topology, run records, structures and derived analyses are preserved here.

A future data manifest should catalogue the externally retained raw files, including filenames, sizes and checksums where available. If long-term public preservation of the complete raw simulation dataset is required, these files may be deposited in an appropriate research-data repository and linked from this README.
The same principle applies to oversized generated analysis files. For example:

`06_MD_analysis/further_investigation_2026/AlphaFold_model/clustering/clusters_FINAL_080.xpm`

is approximately 597 MB and is intentionally excluded through `.gitignore`, while the smaller supporting clustering outputs and documentation remain in the repository.

## Reproducibility and provenance

The repository is being organised so that historical results are not silently presented as newly generated results.

Where possible, files are identified according to their provenance as:

- original 2020 material;
- reconstructed/reorganised historical material; or
- further investigation performed in 2026.

This distinction is particularly important where historical thesis tables have been reconstructed from the final thesis and surviving computational outputs.

## Status

The historical 2020 Master's research material has been preserved and documented separately from the further investigations undertaken in 2026.

The sequence-matched AF3 versus experimental NMR reassessment is complete. Direct evaluation showed that all five AF3 models satisfied all 14 evaluated i→i+4 experimental distance restraints. Broader distance-restraint analysis identified some apparent violations in individual static structures; these require cautious interpretation because NMR-derived distances reflect conformational ensembles and a single static structure is not expected to reproduce every ensemble-derived separation, particularly in flexible regions.

Structural alignment further showed close agreement between AF3 and the historical model within the experimentally relevant SPAM-H1 region, particularly the principal helical region. The reassessment therefore did not identify evidence that the historical computational model provides a superior interpretation of the available experimental NMR data.

Following expert review by Prof. Brian Smith, the historical-model branch will not be pursued further as a publication on the basis of the present results. The original 2020 work remains preserved as a historical computational study, while the 2026 AF3/NMR analysis is retained as a transparent modern reassessment.

The detailed final interpretation is documented in:

`04_AF3_vs_experimental_NMR/notes/FINAL_AF3_NMR_REASSESSMENT_CONCLUSION.md`

## Acknowledgements

The original 2020 Master's research was undertaken at La Trobe University
under the supervision of Prof. Brian Smith.

Prof. Smith also provided the sequence-matched AlphaFold 3 models used in
the 2026 structural reassessment and provided expert feedback on the
interpretation of the historical and contemporary structural evidence.

The author gratefully acknowledges his guidance and support for preserving
this work as a publicly accessible computational research record.
