# build_readme.py
# Simon Hulse
# simonhulse@protonmail.com
# Last Edited: Thu 13 Jun 2024 18:07:34 EDT


from pathlib import Path
import re
import requests

readme_txt = """# CUPID Paper: Experimental Data

This repository provides the experimental datasets which are presented in the following paper:

**{TITLE}**

{AUTHORS}

<sup>1</sup>*{OXFORD}*

<sup>2</sup>*{MANCHESTER}*

<sup>*</sup>`{EMAIL}`

`<INSERT CITATION HERE>`

## Datasets

* `data/camphor/1` - Camphor 2DJ dataset, presented in the {SILONG}, Figure 8.
* `data/dexamethasone/` - Dexamethasone data, presented in the {SISHORT}, Figure 9:

    - `1/` - 2DJ dataset.
    - `2/` - TSE PSYCHE dataset.

* `data/estradiol/` - 17β-estradiol dataset, presented in Figure 3 of the main paper:

    - `1/` - 2DJ dataset.
    - `2/` - PSYCHE dataset.

* `data/quinine/1` - Quinine 2DJ dataset, presented in Figure 2 of the main paper."""

dst = 'README.md'

with open(Path('~/.ghtoken').expanduser(), 'r') as fh:
    token = fh.read().rstrip()

fields_txt = requests.get(
    'https://raw.githubusercontent.com/5hulse/cupid_paper/master/fields.tex',
    headers={
        'accept': 'application/vnd.github.v3.raw',
        'authorization': 'token {}'.format(token)
    },
).text

regex = re.compile(r'.*\{(.*)\}\{(.*)\}')
re.findall(regex, fields_txt)
fields = {key[1:]: value for key, value in re.findall(regex, fields_txt)}

authors = '{SH}<sup>1</sup>, {MN}<sup>2</sup>, {GM}<sup>2</sup> {MF}<sup>1*</sup>'.format(
    SH=fields['SH'],
    MN=fields['MN'],
    GM=fields['GM'],
    MF=fields['MF'],
)

readme_txt = readme_txt.format(
    TITLE=fields['TITLE'],
    AUTHORS=authors,
    OXFORD=fields['OXFORD'],
    MANCHESTER=fields['MANCHESTER'],
    EMAIL=fields['EMAIL'],
    SILONG=fields['SIlong'],
    SISHORT=fields['SIshort'],
)

with open(dst, 'w') as fh:
    fh.write(readme_txt)
