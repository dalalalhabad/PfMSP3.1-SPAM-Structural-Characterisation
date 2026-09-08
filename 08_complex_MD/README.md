# Protein-complex molecular dynamics — historical 2020 workflow

This directory preserves molecular-dynamics simulation material associated
with selected PfMSP3.1 SPAM–C1 inhibitor (C1-INH) complexes investigated
during the original 2020 Master's project.

The complexes originated from the historical protein–protein docking
workflow preserved under:

`../07_protein_docking/`

## Historical workflow

All material in this directory is stored under:

`historical_2020/`

The simulations were performed on selected docked complexes involving
the historical PfMSP3.1 SPAM structural model and C1-INH structures
represented by PDB entries 2OAY and 5DU3.

The four complexes prioritised in the historical workflow were:

- 2OAY complex 2
- 2OAY complex 74
- 5DU3 complex 499
- 5DU3 complex 1266

These complexes had been prioritised during the preceding docking,
ZRANK and/or buried-surface-area analyses.

## Directory organisation

The historical simulations are organised by C1-INH structure and
selected complex.

For example:

`historical_2020/2OAY/complex_2/`

and corresponding directories for the other selected complexes.

Depending on the surviving historical material, individual complex
directories contain combinations of:

- input structures;
- modelling or structure-preparation files;
- molecular-dynamics parameter files;
- topology-related files;
- energy-minimisation records;
- NVT and NPT equilibration records;
- production-MD records;
- intermediate simulation stages; and
- recovered structural outputs.

The exact surviving files differ between complexes because this
repository preserves the material recoverable from the original project
rather than reconstructing files that are no longer available.

## Molecular-dynamics refinement

The selected docked complexes were subjected to molecular-dynamics
refinement during the historical project.

The final thesis reported 250-ns MD investigation of the selected
protein complexes.

These simulations were separate from the triplicate MD simulations of
the isolated historical SPAM model documented under:

`../05_MD_simulations/`

The two workflows should therefore not be conflated:

- isolated SPAM MD investigated the behaviour of the historical SPAM
  structural model; and
- complex MD investigated selected predicted SPAM–C1-INH docking
  configurations.

## Relationship to docking

The docking workflow that generated and prioritised these complexes is
preserved under:

`../07_protein_docking/historical_2020/`

The reconstructed historical docking tables are stored under:

`../10_tables/historical_2020/`

Relevant tables include:

- `Table_5_ZRANK_top20_complexes.csv`
- `Table_6_ZRANK_BSA_before_after_MD.csv`

Table 6 summarises the historical comparison of ZRANK and buried
surface area before and after MD refinement.

## Interpretation

These simulations represent computational refinement of predicted
protein–protein docking configurations.

They should not be interpreted as experimental confirmation of a
specific PfMSP3.1–C1-INH binding mode, binding affinity or physiological
interaction geometry.

The docking and complex-MD results are retained as hypothesis-generating
historical computational analyses.

Later experimental literature concerning PfMSP3 and C1-INH should be
considered independently when interpreting the biological context of
these historical predictions.

## Large simulation files

Complete molecular-dynamics trajectories can be very large and are not
required for a lightweight Git-based research record.

Where complete historical trajectory files are unavailable in the
public repository, the retained setup files, parameter files, logs,
structural outputs and derived results document the surviving
computational workflow.

No missing trajectory or intermediate file has been reconstructed or
replaced with inferred data.

## Provenance

The files in this directory originate from the 2020 Master's project
and were reorganised in 2026 for preservation, transparency and easier
navigation.

Historical filenames and computational outputs have been retained where
practical.

Reorganisation of the files does not imply that the simulations were
rerun in 2026.