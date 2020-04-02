# Quiz Reports

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

* Only works for “Classic Quizzes” on Canvas (not New Quizzes)
* Formatting in the student response is **not** preserved
* Will only output questions of type “Essay Question” on Canvas
* Tool is designed for a *Final Exam* use case and therefore, **should not be run on Quizzes that allow more than one attempt.** Doing so may cause unexpected and/or unreliable behaviour.

## Installation

> Project uses **conda** to manage environment (See official **conda** documentation [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file))

1. Create the environment from the `environment.yml` file

    `$ conda env create -f environment.yml`

2. Activate the new environment

    `$ conda activate quiz_reports_env`

3. Verify that the new environment was installed correctly

    `$ conda env list`

4. Run the Jupyter Notebook in browser

    `$ jupyter notebook`

5. Open `Quiz Reports.ipynb`
6. Once Notebook is open, select **Kernal** > **Restart and Run All** (then follow prompts)