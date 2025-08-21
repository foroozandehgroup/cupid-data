# CUPID Paper: Experimental Data

[![DOI](https://zenodo.org/badge/{REPO_ID}.svg)](https://zenodo.org/badge/latestdoi/{REPO_ID})

This repository provides the experimental datasets which are presented in the following paper:

**{TITLE}**

{AUTHORS}

<sup>1</sup>*{OXFORD}*

<sup>2</sup>*{MANCHESTER}*

<sup>*</sup>`{EMAIL}`

`<INSERT CITATION HERE>`

## Datasets

* `data/camphor/1/` - Camphor 2DJ dataset, presented in the {SI_LONG} ({SI_SHORT}), Figure 9:

    - `pdata/1/` - Processed 2DJ data.
    - `pdata/2/` - Pure-shift spectrum produced using a 45° tilt and projection.

* `data/dexamethasone/` - Dexamethasone data ({SI_SHORT} Figure 10):

    - `1/` - 2DJ dataset.
    - `2/` - TSE-PSYCHE dataset.
    - `1002/` - Reconstructed TSE-PSYCHE dataset (reconstruction done using
      [pshift](http://nmr.chemistry.manchester.ac.uk/sites/default/files/pshift)).

* `data/estradiol/` - 17β-estradiol dataset (main paper Figure 3):

    - `1/` - 2DJ dataset.
    - `2/` - PSYCHE dataset.
    - `1002/` - Reconstructed PSYCHE dataset.

* `data/quinine/1` - Quinine 2DJ dataset (main paper Figure 2):

    - `pdata/1/` - Processed 2DJ spectrum.
    - `pdata/2/` - Pure-shift spectrum produced using a 45° tilt and projection.

## Code

The results present in the paper can be reporduced by running the Jupyter
notebooks within the `code/` directory:

* `code/strychnine/` - Simulated strychnine result ({SI_SHORT} Figure 8).

* `code/camphor/` - Camphor result, ({SI_SHORT} Figure 9).
