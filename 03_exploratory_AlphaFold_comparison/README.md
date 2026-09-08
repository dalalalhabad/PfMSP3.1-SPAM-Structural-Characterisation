# Exploratory AlphaFold comparison — 2026

This directory preserves an exploratory AlphaFold-related investigation
performed during the 2026 reassessment of the historical PfMSP3.1 SPAM
structural model.

## Important sequence-provenance finding

The AlphaFold Database structure examined in this exploratory analysis
corresponds to accession:

`A0A8G1DNL0`

The associated AlphaFold/UniProt sequence contains 121 amino acids.

By contrast, the historical PfMSP3.1 SPAM structural model used in the
2020 Master's project was based on a 139-amino-acid sequence:

`sequence/SPAM_139aa_for_matched_AF_prediction.fasta`

Direct sequence comparison demonstrated that these sequences are not
identical:

- AlphaFoldDB A0A8G1DNL0 sequence length: 121 aa
- Historical SPAM modelling sequence length: 139 aa
- Exact sequence match: no

The AlphaFold structure stored at:

`model/AF_model.pdb`

also contains 121 residues.

Accordingly, A0A8G1DNL0 is not treated as a sequence-matched AlphaFold
prediction or as direct structural validation of the historical 139-aa
SPAM model.

This exploratory branch is retained for analytical provenance and
transparency.

## Files

### Sequence

`sequence/A0A8G1DNL0.fasta`

Sequence associated with the investigated AlphaFoldDB entry.

`sequence/A0A8G1DNL0.txt`

Historical UniProt/entry information associated with A0A8G1DNL0.

`sequence/SPAM_139aa_for_matched_AF_prediction.fasta`

The exact 139-aa SPAM sequence corresponding to the historical
structural-modelling query.

### Model

`model/AF_model.pdb`

AlphaFoldDB structure associated with A0A8G1DNL0. This model contains
121 residues and does not correspond directly to the historical 139-aa
SPAM sequence.

### Confidence

`confidence/AF-A0A8G1DNL0-F1-confidence_v6.json`

Per-residue AlphaFold confidence information associated with A0A8G1DNL0.

## Exploratory molecular-dynamics analysis

A 250-ns molecular-dynamics investigation was subsequently performed on
the A0A8G1DNL0-derived AlphaFold model during the 2026 reassessment.

Simulation records are preserved under:

`../05_MD_simulations/further_investigation_2026/AlphaFold_model/`

and the corresponding analyses are preserved under:

`../06_MD_analysis/further_investigation_2026/AlphaFold_model/`

Because A0A8G1DNL0 does not sequence-match the historical 139-aa SPAM
construct, these analyses are retained as exploratory work and are not
used as direct validation of the historical structural model.

## Subsequent sequence-matched reassessment

Following identification of the sequence mismatch, the structural
reassessment proceeded using the exact historical 139-aa SPAM sequence.

Sequence-matched AlphaFold 3 models supplied by Prof. Brian Smith were
subsequently evaluated against the deposited experimental NMR restraints
associated with the SPAM-H1 region.

That sequence-matched reassessment is documented separately under:

`../04_AF3_vs_experimental_NMR/`

The original externally supplied AlphaFold 3 prediction package is not
redistributed in this public repository. Derived analyses, scripts,
restraint-evaluation results and provenance documentation are retained
in the corresponding reassessment workflow.

## Interpretation

The material in this directory represents a genuine exploratory stage
of the 2026 investigation.

It is preserved because identifying the sequence mismatch was an
important provenance finding that changed the direction of the
subsequent structural reassessment.

Results derived from A0A8G1DNL0 should therefore not be interpreted as
evidence for or against the historical 139-aa PfMSP3.1 SPAM model.