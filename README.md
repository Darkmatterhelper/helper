# Quiz Reports

> Quiz Reports is in BETA. Use at own risk. We are constantly improving performance, usability, and stability.

## Summary

**Quiz Reports** is a Jupyter Notebook and Python application that pulls quiz data from [Canvas LMS](https://github.com/instructure/canvas-lms) to create PDF documents containing student answers to *essay questions*. Application requires the following user inputs:

* Canvas Instance
* Active Canvas Access Token
* Course ID
* Quiz ID


## Output

### `.zip` file containing a PDF per student *(who submitted the quiz)*

* **ID** (randomly-generated, anonymous student identifier)
* **Course name** (as it appears on Canvas)
* **Question text** (as it appears on Canvas)
* **Student's response** (all submitted text -- does not preserving formatting)

> NOTE: all of the above will repeat for as many questions as are in the quiz (on seperate pages)

### `.csv` detailing

* **Student Name** (as it appears on Canvas)
* **Student ID** (UBC student ID)
* **Canvas ID** (Canvas LMS ID)
* **Anonymous ID** (as it appears in the output PDFs)

> NOTE: this table contains sensitive information and should **NOT** be distributed or uploaded anywhere

## Important Caveats

* **Does not work for quizzes with Question Groups**
* Only works for “Classic Quizzes” on Canvas (not New Quizzes)
* Formatting in the student response is **not** preserved
* Will only output questions of type “Essay Question” on Canvas
* Tool is designed for a *Final Exam* use case and therefore, **should not be run on Quizzes that allow more than one attempt.** Doing so may cause unexpected and/or unreliable behaviour.

## Getting Started

> Project uses **conda** to manage environment (See official **conda** documentation [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file))

## Setup (only needs to be done once)

1. Clone repository or download **quiz_reports** from TeamShare (for Sauder Staff)

1. Install [Anaconda](https://www.anaconda.com/distribution/#download-section) (Python 3.7 version)

1. Import environment
    1. Open **Anaconda Navigator** and select **Import**
    1. Name the environment `quiz_reports_env`
    1. Navigate to quiz_reports directory and select environment file:
        * MacOS: `environment_mac.yml`
        * Windows: `environmen_win.yml`
    1. Wait for installation to complete

## Run (do every time)

1. In **Anaconda Navigator**, run `quiz_reports_env` and select **Open with Jupyter Notebook**

1. In the browser, navigate to the **quiz_reports** project folder and select **Quiz Reports.ipynb** (Note this will be located wherever you downloaded or cloaned it in step 1)

1. Select **Kernal** > **Restart & Run All**