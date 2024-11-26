# build_readme.py
# Simon Hulse
# simonhulse@protonmail.com
# Last Edited: Tue 26 Nov 2024 10:45:52 AM EST


from pathlib import Path
import re
import requests


def build_author(name: str, idx: int, orcid: str) -> str:
    return f'{name}<sup>{idx}</sup>: ![ORCID](ORCID-iD_icon_24x24.png) {orcid}'


with open("readme_template.txt", "r") as fh:
    readme_txt = fh.read()

dst = 'README.md'
token_file = Path('~/.ghtoken').expanduser()
github_api_link = 'https://api.github.com/repos/foroozandehgroup/cupid-data'
field_file = 'https://raw.githubusercontent.com/simonhulse/cupid/master/fields.tex'

repo_id = requests.get(github_api_link).json()['id']

# Get paper info
with open(token_file, 'r') as fh:
    token = fh.read().rstrip()
fields_txt = requests.get(
    field_file,
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
    AUTHORS='\n'.join(
            [
                build_author(fields['SH'], 1, fields['SHORCID']),
                build_author(fields['MN'], 2, fields['MNORCID']),
                build_author(fields['GM'], 2, fields['GMORCID']),
                build_author(fields['MF'], 1, fields['MFORCID']),
            ]
    ),
    OXFORD=fields['OXFORD'],
    MANCHESTER=fields['MANCHESTER'],
    EMAIL=fields['MFEMAIL'],
    SI_LONG=fields['SILONG'],
    SI_SHORT=fields['SISHORT'],
)

with open(dst, 'w') as fh:
    fh.write(readme_txt)
