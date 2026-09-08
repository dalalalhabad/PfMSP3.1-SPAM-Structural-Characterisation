# AlphaFold 3 versus experimental NMR reassessment — 2026

This directory contains the sequence-matched 2026 structural reassessment
of the historical PfMSP3.1 SPAM model using AlphaFold 3 (AF3) predictions
and the experimental NMR restraints associated with the SPAM-H1 region.

## Purpose

The purpose of this reassessment was to determine whether modern
sequence-matched AF3 predictions were compatible with the original
experimental NMR evidence and whether the historical computational model
provided a structurally superior explanation of those observations.

The comparison was performed against the underlying experimental NMR
restraints rather than treating the deposited 1PSM coordinate ensemble
as the primary experimental benchmark.

## Sequence-matched AF3 predictions

The AF3 prediction package used the same 139-amino-acid sequence as the
historical PfMSP3.1 SPAM modelling workflow.

The sequence-matched AF3 models were supplied by Prof. Brian Smith.

The original externally supplied AF3 prediction package is retained
outside the public Git repository and is not redistributed here.

This repository instead preserves:

- provenance documentation;
- the historical model;
- the deposited experimental NMR restraint file;
- analysis scripts;
- derived restraint-evaluation results;
- structural-comparison outputs; and
- the final scientific interpretation.

See:

`notes/AF3_input_provenance.md`

## Experimental NMR data

The experimental restraint file used in the reassessment is:

`input/NMR_experimental_data/1PSM.mr`

The historical structural model evaluated against the same restraints is:

`input/historical_model/model.B99990034_original.pdb`

The NMR restraint set was audited before structural evaluation, including
explicit residue-number mapping between the experimental construct and
the historical 139-aa modelling construct.

## Analysis workflow

The analysis scripts are stored under:

`scripts/`

The workflow includes:

1. full AF3 distance-restraint evaluation;
2. consensus violation analysis across AF3 models;
3. independent evaluation of the historical MODELLER model; and
4. structural alignment of the historical model and the sequence-matched
   AF3 predictions.

Scripts:

- `01_AF3_full_NMR_distance_restraint_audit.py`
- `02_AF3_consensus_violation_audit.py`
- `03_historical_model_NMR_restraint_audit.py`
- `04_historical_vs_AF3_structural_alignment.py`

## Derived results

Derived outputs are stored under:

`results/`

These include:

- overall AF3 distance-restraint summaries;
- stratified restraint summaries;
- individual AF3 restraint violations;
- i→i+4 restraint evaluation;
- φ-restraint evaluation;
- consensus AF3 violations;
- historical-model restraint evaluation; and
- historical-versus-AF3 structural RMSD results.

The original externally supplied AF3 coordinate and confidence files are
not included in this public directory.

## Principal findings

All five sequence-matched AF3 models satisfied:

- 27/27 evaluated φ restraints; and
- 14/14 evaluated i→i+4 distance restraints.

Overall distance-restraint satisfaction varied across the five AF3
models, as expected when static predicted structures are compared with
ensemble-derived NMR measurements.

The historical model and AF3 predictions showed close structural
agreement within the experimentally relevant SPAM-H1 region and
particularly within the principal helical segment.

Large full-length RMSD values were dominated by structural differences
outside the locally constrained experimental region and were therefore
not interpreted as evidence that the historical model was superior.

## Interpretation

The reassessment supports compatibility between the sequence-matched AF3
predictions and the available experimental NMR evidence.

It does not demonstrate that the historical computational model provides
a superior explanation of the experimental observations.

The historical model remains preserved as part of the 2020 computational
research record, while this directory documents its transparent
sequence-matched reassessment using modern structure prediction.

The detailed scientific conclusion is available in:

`notes/FINAL_AF3_NMR_REASSESSMENT_CONCLUSION.md`

## Provenance

The original 2020 structural model was retained unchanged.

The original AF3 prediction package supplied by Prof. Brian Smith was also
retained unchanged outside the public Git repository.

Derived analytical outputs generated during the 2026 reassessment are
provided here for transparency, reproducibility and scholarly reference.