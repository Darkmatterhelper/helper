from helpers import get_essay_question_ids, create_quiz_report, get_progress, download_quiz_report, generate_random_id
from reportlab.pdfgen import canvas as pdfcanvas
from dotenv import load_dotenv
from canvasapi import Canvas
import pandas as pd
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


def main():
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
        # print('waiting for progress...')
        progress = get_progress(report_info['progress_url'], AUTH_HEADER)
        if progress == 'completed':
            print('done!\n')
            break

    # Download report
    df = download_quiz_report(report_info, AUTH_HEADER)

    cols = ['name', 'id']
    for c in df.columns.values:
        if c[:7] in essay_question_ids:
            cols.append(c)

    df = df[cols]

    students_df = pd.DataFrame(columns=['Name', 'UBC ID', 'Anonymous ID'])

    dir_path = f'output/COURSE({COURSE_ID})_QUIZ({QUIZ_ID})'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    for index, row in df.iterrows():
        # generate a random id for the student
        anonymous_id = generate_random_id()

        # get UBC id
        ubc_stu_id = get_ubc_id(row['id'])

        # add the random id, student name, and UBC sid to a dataset that will be made into csv
        students_df = students_df.append({'Name': row['name'],
                                          'UBC ID': ubc_stu_id,
                                          'Anonymous ID': anonymous_id},
                                         ignore_index=True)

        # create a pdf
        doc_title = f'{anonymous_id}_{COURSE_ID}_{QUIZ_ID}'
        pdf = pdfcanvas.Canvas(dir_path + '/' + doc_title + '.pdf')
        pdf.save()

    # output to {course_id}_{quiz_id}_students.csv
    students_df.to_csv(
        f'{dir_path}/{COURSE_ID}_{QUIZ_ID}_students.csv', index=False)


def get_ubc_id(canvas_id):
    for s in students:
        for key, val in s.attributes.items():
            if key == 'id':
                if val == canvas_id:
                    return s.attributes['sis_user_id']
    return 'ERROR: UBC id Not Found'


if __name__ == '__main__':
    main()
