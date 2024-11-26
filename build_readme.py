# build_readme.py
# Simon Hulse
# simonhulse@protonmail.com
# Last Edited: Mon 25 Nov 2024 11:20:27 PM EST


from pathlib import Path
import re
import requests

readme_txt = """# CUPID Paper: Experimental Data

[![DOI](https://zenodo.org/badge/{REPO_ID}.svg)](https://zenodo.org/badge/latestdoi/{REPO_ID})

This repository provides the experimental datasets which are presented in the following paper:

**{TITLE}**

{AUTHORS}

<sup>1</sup>*{OXFORD}*

<sup>2</sup>*{MANCHESTER}*

<sup>*</sup>`{EMAIL}`

`<INSERT CITATION HERE>`

## Datasets

* `data/camphor/1` - Camphor 2DJ dataset, presented in the {SI_LONG}, Figure 8.
* `data/dexamethasone/` - Dexamethasone data, presented in the {SI_SHORT}, Figure 9:

    - `1/` - 2DJ dataset.
    - `2/` - TSE PSYCHE dataset.

* `data/estradiol/` - 17β-estradiol dataset, presented in Figure 3 of the main paper:

    - `1/` - 2DJ dataset.
    - `2/` - PSYCHE dataset.

* `data/quinine/1` - Quinine 2DJ dataset, presented in Figure 2 of the main paper."""

dst = 'README.md'
token_file = Path('~/.ghtoken').expanduser()
github_api_link = 'https://api.github.com/repos/foroozandehgroup/cupid-data'

repo_id = requests.get(github_api_link).json()['id']

# Get paper info
with open(token_file, 'r') as fh:
    token = fh.read().rstrip()
fields_txt = requests.get(
    'https://raw.githubusercontent.com/simonhulse/cupid/master/fields.tex',
    headers={
        'accept': 'application/vnd.github.v3.raw',
        'authorization': 'token {}'.format(token)
    },
).text
regex = re.compile(r'.*\{(.*)\}\{(.*)\}')
re.findall(regex, fields_txt)
fields = {key[1:]: value for key, value in re.findall(regex, fields_txt)}

readme_txt = readme_txt.format(
    REPO_ID=repo_id,
    TITLE=fields['TITLE'],
    AUTHORS='{SH}<sup>1</sup>, {MN}<sup>2</sup>, {GM}<sup>2</sup> {MF}<sup>1*</sup>'.format(
        SH=fields['SH'],
        MN=fields['MN'],
        GM=fields['GM'],
        MF=fields['MF'],
    ),
    OXFORD=fields['OXFORD'],
    MANCHESTER=fields['MANCHESTER'],
    EMAIL=fields['MFEMAIL'],
    SI_LONG=fields['SILONG'],
    SI_SHORT=fields['SISHORT'],
)

with open(dst, 'w') as fh:
    fh.write(readme_txt)
