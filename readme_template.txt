# CUPID Paper: Experimental Data & Result Scripts

[![DOI](https://zenodo.org/badge/{REPO_ID}.svg)](https://zenodo.org/badge/latestdoi/{REPO_ID})

This repository provides the experimental datasets and results which are
presented in the following paper:

**{TITLE}**

{AUTHORS}

<sup>1</sup>*{OXFORD}*

<sup>2</sup>*{MANCHESTER}*

<sup>*</sup>`{EMAIL}`

`<INSERT CITATION HERE>`

## Datasets

* `data/estradiol/` - 17β-estradiol dataset (main paper Figure 3):

    - `1/` - 2DJ dataset.
    - `2/` - PSYCHE dataset.
    - `3/` - 2DJ dataset acquired using a higher-concentration sample.

* `data/quinine/1` - Quinine 2DJ dataset (main paper Figure 2):

    - `pdata/1/` - Processed 2DJ spectrum.
    - `pdata/2/` - Pure-shift spectrum produced using a 45° tilt and projection.

* `data/four-multiplets/` - Simulated datasets presented as part of
  the ``Four Multiplets'' result in Figure 6 of the {SI_LONG} ({SI_SHORT}):

    - `run.py` - Python script called to make the data.
    - `make_data.m` - MATLAB script which makes a single 2DJ dataset with Spinach.
    - `pathdef.m` - MATLAB script which defines the path. I found that the
      easiest way to run MATLAB from the command line was to simply place this
      in the working directory.
    - `jres_seq.m` - 2DJ Spinach pulse sequence.
    - `datasets/dataset_[1-5].mat` - The resultant datasets. These can be
      imported into Python using [`scipy.io.loadmat`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.loadmat.html).
    - `datasets/dataset_info.toml` - The shifts and couplings associated with
      each dataset.

* `data/strychnine/` - Simulated strychinine 2DJ dataset ({SI_SHORT} Figure 8):

    - `make_data.m` - MATLAB script which simulates the dataset.
    - `run.fish` - [Fish shell](https://fishshell.com/) command to run
      `make_data.m` from the command line.
    - `fid_2dj.mat` - 2DJ dataset.
    - `pathdef.mat` - See above.
    - `jres_seq.m` - See above.

* `data/camphor/1/` - Camphor 2DJ dataset ({SI_SHORT} Figure 9):

    - `pdata/1/` - Processed 2DJ data.
    - `pdata/2/` - Pure-shift spectrum produced using a 45° tilt and projection.

* `data/dexamethasone/` - Dexamethasone data ({SI_SHORT} Figure 10):

    - `1/` - 2DJ dataset.
    - `2/` - TSE-PSYCHE dataset.

## Jupyter Notebooks and Results

The results presented in the paper can be reproduced by running the Jupyter
notebooks within the `code/` directory.

**You are advised to look at the Quinine and Strychnine notebooks first, as
detailed descriptions are provided in these.**

**To run a particular notebook, make sure that you launch Jupyter Lab inside
one of the directories listed below. I.e. to look at the quinine notebook, make
sure you are in `code/quinine/`.**

* `code/quinine/` - Quinine result (main paper Figure 2).

* `code/estradiol/` - 17β-Estradiol result (main paper Figure 3).

* `code/four-multiplets/` - "Four multiplets" result ({SI_SHORT} Figure 6).

* `code/strychnine/` - Simulated strychnine result ({SI_SHORT} Figure 8).

* `code/camphor/` - Camphor result, ({SI_SHORT} Figure 9).

* `code/dexamethasone/` - Dexamethasone result, ({SI_SHORT} Figure 10).

