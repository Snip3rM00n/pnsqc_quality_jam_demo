# Hybrid POM/LFM Demo for PNSQC Quality Jam

This repository contains the contents of the demo displayed during the PNSQC Quality Jam on January 25, 2024.

## Prerequisites for Setup

The following sections define prerequisites to run the project.  Note, you only need to follow through the Required Prerequisites.

### Required Prerequisites
To set up the repo, make sure you have the following configured and installed.
* Google Chrome installed - https://www.google.com/chrome/
* GNU Make - https://www.gnu.org/software/make/
* Python 3.11 or Higher - https://www.python.org/downloads/
* Poetry for Python - https://python-poetry.org/docs/#installation
* A Virtual Environment created (in project dir is fine)
  * `python3 -m venv ./venv`
* ChromeDriver version matching your version of Google Chrome

### Recommended Prerequisites
* iPython installed - https://ipython.org
* Jupyter installed - https://jupyter.org

## Setting Up

1. Source your virtual environment:
   1. POSIX environments (macOS, Linux): `source ./venv/bin/activate`
   2. Windows CMD: `.\venv\Scripts\activate.bat`
   3. Windows PowerShell: `.\venv\Scripts\activate.ps1`
4. Run `make install-deps`
5. Copy your ChromeDriver to the Bin folder of your Virtual Environment
   6. POSIX environments (macOS, Linux): `cp /path/to/chromedriver ./venv/bin`
   7. Windows Environments: `copy C:\path\to\chromedriver.exe .\venv\Scripts`

## Running the Demo

Once you've met the prerequisites and performed the setup instructions, simply run `make shell` and play around!

### Alternatively

If you wish to use an interpreter other than either iPython or the Python REPL, simply launch your preferred interpreter in interative mode and point it to the `./interative_models.py` file.