# Setup/Run instructions for Windows

> Sauder Specific Instructions

## Setup (only needs to be done once)

1. Download **quiz_reports** from teamshare and put on Desktop *(make sure to get Windows version)*

1. Download and install [Visual Studio Code](https://code.visualstudio.com/download)

1. Install [Git](https://git-scm.com/download/win)

1. Set Git Bash as default terminal on Visual Studio Code
    1. Open Visual Studio Code and open the command palette with `Ctrl + Shift + P`
    1. Type **Select Default Shell**
    1. Select **Git Bash** from options
    1. Select **Terminal** > **New Terminal** (and ensure it opens)

1. Install [Anaconda](https://www.anaconda.com/distribution/#windows) (python 3.7 version)

1. Setup conda
    1. Open **quiz_reports** in Visual Studio Code
    1. Open new terminal with **Terminal** > **New Terminal**
    1. Run `. /c/Anaconda3/etc/profile.d/conda.sh`
    1. Run `conda --version` and ensure version number gets printed
    1. Run `conda env create -f win_environment.yml` and wait for installation to finish
    1. Move on to *Ran it before?* section

## Run (do every time)

1. Open **quiz_reports** in Visual Studio Code

1. Open new terminal with **Terminal** > **New Terminal**

1. Run `. /c/Anaconda3/etc/profile.d/conda.sh` (Run `conda --version` to ensure version number gets printed)

1. Run `conda activate quiz_reports_env`

1. Run `jupyter notebook` (will open default browser)
