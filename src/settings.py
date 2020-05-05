"""
QUIZ_REPORTS: settings

This file is responsible for defining/initializing global variables.

authors:
@markoprodanovic

last edit:
Wednesday, April 03, 2020
"""


def init():

    # Canvas object to provide access to Canvas API
    global course

    # Quiz object representing Canvas quiz specified by user input
    global quiz

    # Object containing information about students in course
    global students

    # Authorization for API Calls
    global auth_header

    # Does this quiz use question bank(s) (default: false)
    global has_question_bank
