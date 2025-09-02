# CUPID Paper: Experimental Data & Result Scripts

[![DOI](https://zenodo.org/badge/814870133.svg)](https://zenodo.org/badge/latestdoi/814870133)

This repository provides the experimental datasets and results which are
presented in the following paper:

**Full-Signal Ultrahigh-Resolution NMR**

Simon G. Hulse<sup>1</sup> ![ORCID](ORCID-iD_icon_16x16.png) https://orcid.org/0000-0002-5822-6198

Mathias Nilsson<sup>2</sup> ![ORCID](ORCID-iD_icon_16x16.png) https://orcid.org/0000-0003-3301-7899

Gareth A. Morris<sup>2</sup> ![ORCID](ORCID-iD_icon_16x16.png) https://orcid.org/0000-0002-4859-6259

Mohammadali Foroozandeh<sup>1</sup> ![ORCID](ORCID-iD_icon_16x16.png) https://orcid.org/0000-0001-8937-3118

<sup>1</sup>*Chemistry Research Laboratory, University of Oxford, 12 Mansfield Rd, Oxford, OX1 3TA, UK*

<sup>2</sup>*Department of Chemistry, University of Manchester, Oxford Road, Manchester M13 9PL, UK*

<sup>*</sup>`mohammadali.foroozandeh@chem.ox.ac.uk`

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
  the ``Four Multiplets'' result in Figure 6 of the Supporting Information (SI):

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

* `data/strychnine/` - Simulated strychinine 2DJ dataset (SI Figure 8):

    - `make_data.m` - MATLAB script which simulates the dataset.
    - `run.fish` - [Fish shell](https://fishshell.com/) command to run
      `make_data.m` from the command line.
    - `fid_2dj.mat` - 2DJ dataset.
    - `pathdef.mat` - See above.
    - `jres_seq.m` - See above.

* `data/camphor/1/` - Camphor 2DJ dataset (SI Figure 9):

    - `pdata/1/` - Processed 2DJ data.
    - `pdata/2/` - Pure-shift spectrum produced using a 45° tilt and projection.

* `data/dexamethasone/` - Dexamethasone data (SI Figure 10):

    - `1/` - 2DJ dataset.
    - `2/` - TSE-PSYCHE dataset.

## Jupyter Notebooks and Results

The results presented in the paper can be reproduced by running the Jupyter
notebooks within the `code/` directory.

**You are advised to look at the Quinine and Strychnine notebooks first, as
detailed descriptions are provided in these.**

* `code/quinine/` - Quinine result (main paper Figure 2).

* `code/estradiol/` - 17β-Estradiol result (main paper Figure 3).

* `code/four-multiplets/` - "Four multiplets" result (SI Figure 6).

* `code/strychnine/` - Simulated strychnine result (SI Figure 8).

* `code/camphor/` - Camphor result, (SI Figure 9).

* `code/dexamethasone/` - Dexamethasone result, (SI Figure 10).

