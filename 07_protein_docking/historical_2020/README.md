# Protein–protein docking — historical 2020 workflow

This directory preserves the protein–protein docking analyses performed
during the original 2020 Master's project on the PfMSP3.1 SPAM domain.

The docking work investigated predicted interactions between the
historical SPAM structural model and two C1 inhibitor (C1-INH) structures.

The material in this directory should be interpreted as historical,
hypothesis-generating computational work and not as experimental proof
of a physiological PfMSP3.1–C1-INH interaction.

## Organisation

Historical docking material is stored under:

`historical_2020/`

and is organised according to the two C1-INH structures used in the
original workflow:

- `historical_2020/2OAY/`
- `historical_2020/5DU3/`

Each branch contains retained docking, scoring and buried-surface-area
analysis files from the original project.

## ZDOCK workflow

Protein–protein docking was performed using ZDOCK.

For each C1-INH structure and each SPAM structural replicate, the docking
workflow generated a large set of predicted complexes.

The retained ZDOCK directories contain historical run records and selected
structures recovered from the original 2020 project.

The docking results were subsequently rescored using ZRANK.

The top ZRANK-scoring complexes reported in the thesis are summarised in:

`../10_tables/historical_2020/Table_5_ZRANK_top20_complexes.csv`

## Buried surface area analysis

Buried surface area (BSA) was evaluated for selected docked complexes.

BSA-related files are retained within the corresponding `BSA/`
directories under the `2OAY` and `5DU3` branches.

These folders include the historical receptor, ligand and complex
surface-area outputs together with selected docked structures.

## Selected complexes

Four complexes were prioritised in the original workflow for subsequent
molecular-dynamics investigation:

- 2OAY complex 2
- 2OAY complex 74
- 5DU3 complex 499
- 5DU3 complex 1266

These complexes were selected on the basis of the historical docking,
ZRANK and/or buried-surface-area analyses.

Their corresponding molecular-dynamics simulations are preserved under:

`../08_complex_MD/historical_2020/`

## Historical result tables

The reconstructed historical thesis tables associated with the docking
workflow are stored under:

`../10_tables/historical_2020/`

Relevant tables include:

- `Table_5_ZRANK_top20_complexes.csv`
- `Table_6_ZRANK_BSA_before_after_MD.csv`

The accompanying README in that directory explains how those tables were
reconstructed from the final thesis and surviving computational outputs.

## Interpretation

The docking analyses were performed as computational screening and
structural-hypothesis generation.

Docking scores, ZRANK values and buried surface area are not direct
evidence of physiological binding, binding affinity or biological
relevance.

The results should therefore be interpreted together with the broader
historical modelling workflow and, where relevant, later experimental
literature on PfMSP3 and C1-INH.

## Provenance

The files in this directory were recovered from the original 2020
Master's project and reorganised in 2026 for preservation and clearer
navigation.

Original historical files are retained where available.

The repository does not attempt to reconstruct missing docking outputs
or assign interpretations that cannot be supported by the surviving
project files.