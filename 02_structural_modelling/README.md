# Structural modelling

This directory contains the historical structural-modelling work associated with the 2020 Master's project on the PfMSP3.1 SPAM domain.

The material is organised into the final thesis modelling workflow and earlier exploratory modelling attempts.

## Final thesis modelling workflow

### CCBuilder

`CCBuilder/ccbuilder_model.pdb`

Contains the coiled-coil structural model used as part of the final modelling workflow.

### MODELLER

`MODELLER/`

This directory contains the final MODELLER workflow associated with the selected historical SPAM structural model.

Subdirectories include:

- `input/` — template and alignment files
- `scripts/` — MODELLER modelling and restraint scripts
- `logs/` — the complete MODELLER run log
- `output/` — selected model output

The selected final model is:

`MODELLER/output/model.B99990034.pdb`

The historical MODELLER run generated 100 models. Model 34 was selected in the thesis because it had the lowest reported MODELLER objective-function value among the top-scoring models considered.

The corresponding scoring information is preserved in:

`../10_tables/historical_2020/Table_4_MODELLER_objective_function_DOPE.csv`

The files in the final MODELLER workflow were verified against the original 2020 project files by checksum during repository reconstruction.

## Historical exploratory modelling

`historical_exploratory_modelling/`

This directory preserves earlier modelling attempts recovered from the original project files.

These files are retained for provenance and should not be confused with the final thesis modelling workflow.

### 1PSM attempt

`historical_exploratory_modelling/1PSM_attempt/`

Contains an earlier modelling attempt involving 1PSM-related sequence, template and MODELLER files.

The retained files include:

- 1PSM structure and sequence material
- alignment files
- an early MODELLER script
- `model.B99990094.pdb`

This model was not the final structural model used in the thesis.

### 1COS attempt

`historical_exploratory_modelling/1COS_attempt/`

Contains an exploratory modelling workflow involving 1COS/1PSM template material.

The retained MODELLER script includes explicit alpha-helical restraints and inter-residue distance restraints.

The retained files include:

- 1COS and 1PSM structural/template material
- sequence files
- alignment files
- exploratory MODELLER script
- `model.B99990001.pdb`
- `model.preCD55.pdb`

These models were exploratory and were not the final selected thesis model.

## Provenance

The exploratory files were recovered from the original 2020 project directory and added to this repository in 2026.

Screenshots, duplicate files, temporary files, zero-byte files and non-essential desktop artefacts were not copied into this reconstructed workflow.

The purpose of preserving the exploratory material is to document the historical modelling process without mixing preliminary models with the final thesis result.
