You are advised to look at the Quinine and Strychnine notebooks first, as
detailed descriptions are provided in these.

To run a particular notebook, make sure that you launch Jupyter Lab inside
one of the directories listed below. I.e. to look at the quinine notebook, make
sure you are in `code/quinine/` when you run Jupyter Lab.

## Setup

The following commands are for a UNIX shell.

    $ python3.13 -m venv .venv
    $ # The command below is for fish shell (my preferred shell)
    $ # If you use bash, remove the `.fish` suffix
    $ # If you use csh, replace the `.fish` suffix with `.csh`
    $ source .venv/bin/activate.fish
    $ pip install --upgrade pip
    $ pip install -r requirements.txt
    $ jupyter lab
