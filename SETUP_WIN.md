# Setup/Run instructions for Windows

## Setup (only needs to be done once)

1. Clone repository or download **quiz_reports** from teamshare (for Sauder Staff)

1. Download and install [Visual Studio Code](https://code.visualstudio.com/download)

1. Install [Git](https://git-scm.com/download/win)

1. Set Git Bash as default terminal on Visual Studio Code
    1. Open Visual Studio Code and open the command palette with `Ctrl + Shift + P`
    1. Type **Select Default Shell**
    1. Select **Git Bash** from options
    1. From menu, select **Terminal** > **New Terminal** (and ensure it opens)

1. Install [Anaconda (Python 3.7 Version)](https://www.anaconda.com/distribution/#download-section) (take note of install location)

1. Setup conda
    1. Open **quiz_reports** in Visual Studio Code
    1. Open new terminal with **Terminal** > **New Terminal**
    1. Run `. /c/Anaconda3/etc/profile.d/conda.sh` (path to `Anaconda3` may vary depending on install location)
    1. Run `conda --version` and ensure version number gets printed
    1. Run `conda env create -f environment_win.yml` and wait for installation to finish

## Run (do every time)

1. Open **quiz_reports** in Visual Studio Code

1. Open new terminal with **Terminal** > **New Terminal**

1. Run `. /c/Anaconda3/etc/profile.d/conda.sh` (Path may vary based on install location, run `conda --version` to ensure version number gets printed)

1. Run `conda activate quiz_reports_env`

1. Run `jupyter notebook` (will open default browser)
