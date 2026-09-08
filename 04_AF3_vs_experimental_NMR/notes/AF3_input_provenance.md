# AF3 input provenance

## Source

The sequence-matched AlphaFold 3 prediction package used in this
reassessment was supplied by Prof. Brian Smith for comparison with the
experimental NMR evidence associated with the PfMSP3/SPAM-H1 region.

The original supplied prediction archive is retained unchanged outside
the public Git repository and is not redistributed here.

Original archive filename:

`PfMSP3pt1-2774654e-f422-44c5-9c56-f562b85e2029.tar`

## Prediction input

Job name:

`PfMSP3pt1`

Number of protein chains:

1

Input sequence length:

139 aa

Input sequence:

`DDQKDIEAYKKAKQASQDAEQAAKDAENASKEAEEAAKEAVNLKESDKSYTKAKEACTAASKAKKAVETALKAKDDAETALKTSETPEKPSRINLFSRKTKEYAEKAKNAYEKAKNAYQKANQAVLKAKEASSYDYILG`

This is the same historical 139-aa sequence used in the original
PfMSP3.1 structural-characterisation workflow.

## Prediction models supplied

The original external prediction package contained five AF3 coordinate
models:

- `PfMSP3pt1_sample_0.cif`
- `PfMSP3pt1_sample_1.cif`
- `PfMSP3pt1_sample_2.cif`
- `PfMSP3pt1_sample_3.cif`
- `PfMSP3pt1_sample_4.cif`

Five corresponding summary-confidence JSON files were also supplied.

These original externally supplied AF3 files are retained outside the
public Git repository.

Derived results generated from their analysis are preserved under:

`../results/`

and the scripts used for the reassessment are preserved under:

`../scripts/`

## Analysis principle

The AF3 models were evaluated directly against the original experimental
NMR restraints associated with the SPAM-H1 region.

The deposited 1PSM coordinate ensemble was not treated as the primary
experimental benchmark because those coordinates represent a structural
interpretation of the underlying experimental NMR data.

Structure-to-structure comparison with experimental or historical
coordinates was therefore treated as complementary context rather than
a replacement for direct restraint evaluation.

## Public-repository provenance

This public repository contains:

- the historical MODELLER model;
- the deposited experimental NMR restraint file;
- AF3-input provenance documentation;
- restraint-analysis scripts;
- derived AF3 restraint-evaluation results;
- historical-model restraint evaluation;
- structural-comparison outputs; and
- the final reassessment conclusion.

The original externally supplied AF3 archive, coordinate files and
confidence files are not redistributed.