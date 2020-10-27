# Quiz Response PDFs
> - quiz-response-pdfs
> - python>=3.7
> - canvasapi>=2.0.0
## Summary 

**Quiz Response PDFs (quiz-response-pdfs)** is a Jupyter Notebook and Python application that pulls quiz data from [Canvas LMS](https://github.com/instructure/canvas-lms) to create PDF documents containing student answers to _essay questions_. This was developed to allow essay type questions to be run through Turnitin. The application requires the following user inputs:

- Canvas Instance
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
_Are you Sauder Operations Staff? Please go [here]([sauder-ops-guide.md](https://github.com/saud-learning-services/instructions-and-other-templates/blob/master/sauder-ops-guide-jupyter-env-and-launch.md#-ran-it-before-start-here)) for detailed instructions. ("The Project", or "the-project" is "quiz-response-pdfs" or "Quiz Response PDFs")._

### General
> Project uses **conda** to manage environment (See official **conda** documentation [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file))

1. Clone **quiz-response-pdfs** repository

2. Ensure you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed (Python 3.7 version)

3. Import environment (once): `$ conda env create -f environment.yml`

4. Run (every time):
   1. `$ conda activate quiz-response-pdfs`
   2. `$ jupyter notebook`
   3. Select **Kernal** > **Restart & Run All**
