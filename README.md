# Canvas Quiz Response PDFs

> - name: canvas-quiz-response-pdfs
> - ops-run-with: jupyter
> - python>=3.7
> - canvasapi>=2.0.0
> - supports universal environment 🌎

## Summary

**Canvas Quiz Response PDFs (quiz-response-pdfs)** is a Jupyter Notebook and Python application that pulls quiz data from [Canvas LMS](https://github.com/instructure/canvas-lms) to create PDF documents containing student answers to _essay questions_. This was developed to allow essay type questions to be run through Turnitin. The application requires the following user inputs:

- Canvas Instance (i.e. https://ubc.instructure.com)
- Active Canvas Access Token
- Course ID
- Quiz ID
- Question Banks (users will need to specify whether or not the quiz uses Question Banks)

## Output

### `.zip` file containing a PDF per student _(who submitted the quiz)_

- **ID** (randomly-generated, anonymous student identifier)
- **Course name** (as it appears on Canvas)
- **Question text** (as it appears on Canvas)
- **Student's response** (all submitted text -- does not preserving formatting)

> NOTE: all of the above will repeat for as many questions as are in the quiz (on seperate pages)

### `.csv` detailing

- **Student Name** (as it appears on Canvas)
- **Student ID** (UBC student ID)
- **Canvas ID** (Canvas LMS ID)
- **Anonymous ID** (as it appears in the output PDFs)

> NOTE: this table contains sensitive information and should **NOT** be distributed or uploaded anywhere

## :warning: Important Caveats

- Only works for “Classic Quizzes” on Canvas (not New Quizzes)
- Formatting in the student response is **not** preserved
- Will only output questions of type “Essay Question” on Canvas
- Tool is designed for a _Final Exam_ use case and therefore, **should not be run on Quizzes that allow more than one attempt.** Doing so may cause unexpected and/or unreliable behaviour.

## Getting Started

### Sauder Operations

_Are you Sauder Operations Staff? Please go [here](TODO) for detailed instructions to run in Jupyter. ("The Project", or "the-project" is "canvas-quiz-response-pdfs" or "Canvas Quiz Response PDFs")._

### General (terminal instructions)

> Project uses **conda** to manage environment (See official **conda** documentation [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file))

#### First Time

1. Ensure you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed (Python 3.7 version)
1. Clone **canvas-quiz-response-pdfs** repository
1. Import environment (once): `$ conda env create -f environment.yml`

#### Every Time

1. Run:
   1. navigate to your directory `$ cd YOUR_PATH/canvas-quiz-response-pdfs`
   1. activate the environment (see step 3 on first run) `$ conda activate canvs-quiz-response-pdfs`
   1. run the script and follow prompts in terminal `$ python src/quiz_response_pdfs.py`
