"""
QUIZ REPORTS: interface

authors:
@markoprodanovic

last edit:
Monday, May 04, 2020
"""

import getpass
from canvasapi import Canvas
from termcolor import cprint
from util import shut_down
import settings


def get_user_inputs_test():
    url = 'https://ubc.test.instructure.com/'
    token = ''
    auth_header = {'Authorization': f'Bearer {token}'}
    course_id = None 
    quiz_id = None
    has_question_bank = False #or False

    canvas = Canvas(url, token)
    course = canvas.get_course(course_id)
    students = course.get_users(enrollment_type='student')
    quiz = course.get_quiz(quiz_id)

    # set course, quiz, students and auth_header as global variables
    settings.course = course
    settings.quiz = quiz
    settings.students = students
    settings.auth_header = auth_header
    settings.has_question_bank = has_question_bank

    # return inputs dictionary
    return url, course_id, quiz_id

def get_user_inputs():
    """Prompt user for required inputs. Queries Canvas API throughout to check for
    access and validity errors. Errors stop execution and print to screen.

    Returns:
        Dictionary containing inputs
    """

    # prompt user for url and token
    url = input('Canvas Instance URL: ')

    token = getpass.getpass('Please enter your token: ')
    auth_header = {'Authorization': f'Bearer {token}'}

    # Canvas object to provide access to Canvas API
    canvas = Canvas(url, token)

    # get user object
    try:
        user = canvas.get_user('self')
        cprint(f'\nHello, {user.name}!', 'green')
    except Exception:
        shut_down(
            """
            ERROR: could not get user from server.
            Please ensure token is correct and valid and ensure using the correct instance url.
            """
        )

    # get course object
    try:
        course_id = input('Course ID: ')
        course = canvas.get_course(course_id)
    except Exception:
        shut_down(
            f'ERROR: Course not found [ID: {course_id}]. Please check course number.')

    # get students from course
    try:
        students = course.get_users(enrollment_type='student')
    except Exception:
        shut_down(
            'ERROR: Not able to get students from course. Ensure course has enrolled students.')

    # get the quiz from course
    try:
        quiz_id = input('Quiz ID: ')

        quiz = course.get_quiz(quiz_id)
    except Exception:
        shut_down(
            f'ERROR: Quiz not found [ID: {quiz_id}]. Please check quiz number.')

    question_bank_input = input('Does this quiz use Question Bank(s)? [y/n]: ')

    if question_bank_input == 'y' or question_bank_input == 'Y':
        has_question_bank = True
    else:
        has_question_bank = False
    
    include_questions_in_pdf = input('Would you like questions to appear in the output PDFs? [y/n]: ')

    if include_questions_in_pdf == 'y' or include_questions_in_pdf == 'Y':
        include_questions = True
    else:
        include_questions = False

    # prompt user for confirmation
    _prompt_for_confirmation(user.name, course.name, quiz.title, 
                             has_question_bank, include_questions)

    # set course, quiz, students and auth_header as global variables
    settings.course = course
    settings.quiz = quiz
    settings.students = students
    settings.auth_header = auth_header
    settings.has_question_bank = has_question_bank
    settings.include_questions = include_questions

    # return inputs dictionary
    return url, course_id, quiz_id


def _prompt_for_confirmation(user_name, course_name, quiz_title, has_question_bank, include_questions):
    """Prints user inputs to screen and asks user to confirm. Shuts down if user inputs
    anything other than 'Y' or 'y'. Returns otherwise.

    Args:
        user_name (string): name of user (aka. holder of token)
        course_name (string): name of course returned from Canvas
        quiz_title (string): name of quiz returned from Canvas course object
        has_question_bank (boolean)
        include_questions (boolean)

    Returns:
        None -- returns only if user confirms

    """
    cprint('\nConfirmation:', 'blue')
    print(f'USER:  {user_name}')
    print(f'COURSE:  {course_name}')
    print(f'QUIZ:  {quiz_title}')
    print(f'HAS QUESTION BANK: {has_question_bank}')
    print(f"INCLUDE Q'S in PDF: {include_questions}")
    print('\n')

    confirm = input(
        'Would you like to continue using the above information? [y/n]: ')

    print('\n')

    if confirm == 'y' or confirm == 'Y':
        return
    elif confirm == 'n' or confirm == 'N':
        shut_down('Exiting...')
    else:
        shut_down('ERROR: Only accepted values are y and n')
