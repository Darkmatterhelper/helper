# Quiz Reports

## Summary

Quiz reports is a jupyter notebook and python script that interacts with the [Canvas LMS](https://github.com/instructure/canvas-lms) to pull quiz reponse data for a specified quiz. Given a valid quiz id, the tool outputs:

### `.zip` file containing a PDF per student detailing

* Id (randomly-generated, anonymous student identifier)

* Question text (as it appears on Canvas)

* The student's response (as it was submitted by the student)

> NOTE: question text and student reponse will repeat for as many questions as are in the quiz

### `.csv` detailing

* Student name (as it appears on Canvas)

* Student id (UBC student id)

* Anonymous id (as it appears in the output PDF's)

> NOTE: this table contains sensitive information and should **NOT** be distributed or uploaded anywhere

## Details

* The Quiz Reports tool is designed for a *Final Exam* use case and therefore, **should not be run on Quizzes that allow more than one attempt.** Doing so may cause unexpected and/or unreliable behaviour.

* All workflow states will be valid for the CSV so any of these can appear ['untaken', 'pending_review', 'complete', 'settings_only', 'preview'] . However, PDFs will only be made for submissions with a workflow_state of pending review  OR completed

<!-- REMOVE THIS SOON -->
<!-- * The [workflow state](https://canvas.instructure.com/doc/api/quiz_submissions.html) for each submission must be `complete` or `pending_review` in order for a PDF to be outputted. Other workflow states will appear in the CSV however won't have corresponding PDFs. -->

## Installation

TODO
