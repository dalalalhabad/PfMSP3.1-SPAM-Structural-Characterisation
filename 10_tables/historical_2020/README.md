# Historical thesis tables (2020)

This folder contains reconstructed result tables reported in the 2020 Master's thesis on structural characterisation of the PfMSP3.1 SPAM domain.

The tables are preserved as historically reported in the thesis and are linked to the corresponding original modelling, docking and molecular-dynamics files retained elsewhere in this repository.

## Table 4 — MODELLER model scoring

`Table_4_MODELLER_objective_function_DOPE.csv`

Reproduces thesis Table 4:

"Comparison of MODELLER objective function values and DOPE scores for the top 10 models."

The historical workflow generated 100 MODELLER models. The thesis compared MODELLER objective-function and DOPE values for the selected top-scoring models.

Model 34 was selected as the final SPAM structural model because it had the lowest reported MODELLER objective-function value.

Important: this CSV preserves the values as reported in the thesis. It should not be interpreted as a global ranking of all 100 generated models by DOPE score.

## Table 5 — ZRANK scoring of docked complexes

`Table_5_ZRANK_top20_complexes.csv`

Reproduces thesis Table 5:

"ZRANK scoring of the top 20 complexes for each replicate."

Three SPAM structural replicates were docked against both C1-INH structures (5DU3 and 2OAY). For each target and replicate, 2,000 ZDOCK complexes were rescored using ZRANK. This table contains the top 20 ZRANK-scoring complexes reported in the thesis.

The underlying 2,000-pose ZRANK output files are retained in the historical protein-docking workflow under `07_protein_docking/`.

## Table 6 — ZRANK and BSA before and after MD

`Table_6_ZRANK_BSA_before_after_MD.csv`

Reproduces thesis Table 6:

"The ZRANK score and BSA of complexes before and after MD simulation."

Four complexes were taken forward for molecular-dynamics analysis:

- 5DU3: complexes 1266 and 499
- 2OAY: complexes 74 and 2

The table reports ZRANK scores and buried surface area (BSA) before and after the 250-ns complex MD simulations.

The corresponding docking structures, MD files and post-MD comparison material are retained under `07_protein_docking/` and `08_complex_MD/`.
