"""
QUIZ_REPORTS: settings

This file is responsible for defining/initializing global variables.

authors:
@markoprodanovic

last edit:
Wednesday, Nov 10, 2021
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# Canvas object to provide access to Canvas API
course = None

# Quiz object representing Canvas quiz specified by user input
quiz = None

# Object containing information about students in course
students = None

# Authorization for API Calls
auth_header = None

# Does this quiz use question bank(s) (default: false)
has_question_bank = None

# Should the output include questions
include_questions = None
