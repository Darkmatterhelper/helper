# Quiz Reports

## Summary

Quiz reports is a jupyter notebook and python script that interacts with the [Canvas LMS](https://github.com/instructure/canvas-lms) to pull quiz reponse data for a specified quiz. Given a valid quiz id, the tool outputs:

### `.zip` file with a PDF per student detailing

* Id (randomly-generated, anonymous student identifier)

* Question text (as it appears on Canvas)

* The student's response (as it was submitted by the student)

> NOTE: question text and student reponse will repeat for as many questions as are in the quiz


### `.csv` detailing

* Student name (as it appears on Canvas)

* Student id (UBC student id)

* Anonymous id (as it appears in the output PDF's)

> NOTE: this table contains sensitive information and should **NOT** be distributed or uploaded anywhere

## Installation

TODO