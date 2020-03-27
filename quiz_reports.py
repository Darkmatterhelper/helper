from helpers import get_essay_question_ids, create_quiz_report, get_progress, download_quiz_report

from dotenv import load_dotenv
from canvasapi import Canvas
import requests
import pprint
import json
import os

load_dotenv()
pp = pprint.PrettyPrinter(indent=4)

# User Input
URL = os.getenv('URL')
TOKEN = os.getenv('TOKEN')
COURSE_ID = os.getenv('COURSE_ID')
QUIZ_ID = os.getenv('QUIZ_ID')

# Authorization for API Calls
AUTH_HEADER = {'Authorization': f'Bearer {TOKEN}'}

# Calls for course and student info
canvas = Canvas(URL, TOKEN)
course = canvas.get_course(COURSE_ID)
students = course.get_users(enrollment_type='student')

# Getting a list of essay question ids to filter with
quiz = course.get_quiz(QUIZ_ID)
questions = quiz.get_questions()
essay_question_ids = get_essay_question_ids(questions)

# Post report and get info
report_info = create_quiz_report(URL,
                                 AUTH_HEADER,
                                 COURSE_ID,
                                 QUIZ_ID,
                                 'student_analysis')

print('Creating quiz report...\n')
while True:
    print('waiting for progress...')
    progress = get_progress(report_info['progress_url'], AUTH_HEADER)
    if progress == 'completed':
        print('done!\n')
        break

# Download report
download_quiz_report(report_info, AUTH_HEADER)


# reports = filter(
#     lambda r: (r.report_type == 'student_analysis'),
#     reports
# )

# for report in reports:
#     pp.pprint(report.attributes)

# submissions = quiz.get_all_quiz_submissions()

# allowed_wf_states = ['untaken',
#                      'pending_review',
#                      'complete',
#                      'settings_only',
#                      'preview']

# filtered_subs = filter(
#     lambda sub: (sub.workflow_state in allowed_wf_states),
#     submissions
# )

# for item in submissions:
#     pp.pprint(item.attributes)

# count = 0
# for sub in filtered_subs:
# questions = submissions[0].get_submission_questions()

# for q in questions:
#     pp.pprint(q.answer)
