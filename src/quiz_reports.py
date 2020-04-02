"""
QUIZ REPORTS: main

authors:
@markoprodanovic

last edit:
Wednesday, April 02, 2020
"""

from helpers import get_essay_question_ids, create_quiz_report, get_progress, download_quiz_report, generate_random_id, draw_my_ruler
from reportlab.pdfgen import canvas as pdfcanvas
from interface import get_user_inputs
from dotenv import load_dotenv
from canvasapi import Canvas
from util import shut_down
from shutil import rmtree
import pandas as pd
import settings
import requests
import zipfile
import pprint
import json
import os

# for printing neatly formatted objects (used for debugging)
load_dotenv()
pp = pprint.PrettyPrinter(indent=4)


def main():

    # initialize global variables - call only once
    settings.init()

    # get user inputs
    url, course_id, quiz_id = get_user_inputs()

    # get quiz questions and save ids of essay questions
    questions = settings.quiz.get_questions()
    essay_question_ids = get_essay_question_ids(questions)

    # create a new quiz report on Canvas
    try:
        print(f'Creating Canvas quiz report for: {settings.quiz.title}...\n')
        post_report_res = create_quiz_report(url, course_id, quiz_id)
        progress = get_progress(post_report_res['progress_url'], 1)
        assert progress == 'completed'
    except Exception:
        shut_down(
            f'ERROR: Failed to create Canvas quiz report for: {settings.quiz.title}.')

    report_info = get_quiz_report(
        url, course_id, quiz_id, post_report_res['id'])

    # download raw report that was just generated
    df = download_quiz_report(report_info)

    # reduce dataframe columns name, id and any question columns
    cols = ['name', 'id']
    for c in df.columns.values:
        if c[:7] in essay_question_ids:
            cols.append(c)
    df = df[cols]

    # remove name and id so we're only left with question column names - used later
    cols.remove('name')
    cols.remove('id')

    # make students dataframe
    students_df = pd.DataFrame(
        columns=['Name', 'UBC ID', 'Canvas ID', 'Anonymous ID'])

    # make output directory for quiz
    dir_path = f'output/COURSE({course_id})_QUIZ({quiz_id})'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # make outpit subdirectory for pdfs - delete old data if any is there
    pdf_dir_path = dir_path + '/pdfs'
    if os.path.exists(pdf_dir_path):
        rmtree(pdf_dir_path)

    os.makedirs(pdf_dir_path)

    for index, row in df.iterrows():
        # generate a random id for the student
        anonymous_id = generate_random_id()

        # get UBC id
        ubc_stu_id = get_ubc_id(row['id'])

        # add the random id, student name, and UBC sid to a dataset that will be made into csv
        students_df = students_df.append({'Name': row['name'],
                                          'UBC ID': ubc_stu_id,
                                          'Canvas ID': row['id'],
                                          'Anonymous ID': anonymous_id},
                                         ignore_index=True)

        # create a pdf
        doc_title = f'{anonymous_id}_{course_id}_{quiz_id}'

        pdf = pdfcanvas.Canvas(pdf_dir_path + '/' + f'{doc_title}.pdf')
        # draw_my_ruler(pdf)

        # set title for pdf
        pdf.setTitle(doc_title)

        for c in cols:

            # print anonymous id above each question
            pdf.setFont('Courier-Bold', 14)
            pdf.drawString(50, 750, anonymous_id)

            lines = 0
            text = pdf.beginText(50, 700)
            text.setFont('Courier', 12)

            # add question text
            text, lines, pdf = wrap_text_line(text, c, lines, pdf)

            # add space
            text.textLine(' ')
            lines += 1

            # add student response
            text, lines, pdf = wrap_text_line(text, str(row[c]), lines, pdf)
            pdf.drawText(text)

            # add page break for next question/response
            pdf.showPage()
            lines = 0

        # save pdf
        pdf.save()

    # output to {course_id}_{quiz_id}_students.csv
    students_df.to_csv(
        f'{dir_path}/{course_id}_{quiz_id}_students.csv', index=False)

    # Call the function to retrieve all files and folders of the assigned directory
    filePaths = retrieve_file_paths(pdf_dir_path)

    # writing files to a zipfile
    zip_file = zipfile.ZipFile(pdf_dir_path + '.zip', 'w')
    with zip_file:
        # writing each file one by one
        for file in filePaths:
            arcname = file[len(dir_path) + 1:]
            zip_file.write(file, arcname)

    print(pdf_dir_path + '.zip file is created successfully!')
    rmtree(pdf_dir_path)


def get_quiz_report(base_url, course_id, quiz_id, report_id):
    url = f'{base_url}/api/v1/courses/{str(course_id)}/quizzes/{str(quiz_id)}/reports/{str(report_id)}'

    payload = {'include': '[file, progress]'}

    r = requests.get(url, headers=settings.auth_header, data=payload)

    data = json.loads(r.text)

    return(data)


def wrap_text_line(pdf_txt, raw_txt, lines, pdf):
    while len(raw_txt) > 0:

        if (lines >= 45):
            pdf.drawText(pdf_txt)
            pdf.showPage()
            pdf_txt = pdf.beginText(50, 750)
            pdf_txt.setFont('Courier', 12)
            lines = 0

        # take off the first 70 characters from str
        if len(raw_txt) <= 60:
            pdf_txt.textLine(raw_txt)
            lines += 1
            return pdf_txt, lines, pdf
        else:
            line = raw_txt[0:60]
            raw_txt = raw_txt[60:]

            if ' ' in raw_txt:
                split = raw_txt.split(' ', 1)
                line = line + split[0]
                raw_txt = split[1]
            else:
                line = line + raw_txt
                raw_txt = ''

            pdf_txt.textLine(line)
            lines += 1

    return pdf_txt, lines, pdf


def get_ubc_id(canvas_id):
    for s in settings.students:
        for key, val in s.attributes.items():
            if key == 'id':
                if val == canvas_id:
                    return s.attributes['sis_user_id']
    return 'ERROR: UBC id Not Found'


# A function to return all file paths of the particular directory
def retrieve_file_paths(dirName):

    # setup file paths variable
    filePaths = []

    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dirName):
        for filename in files:
            # Create the full filepath by using os module.
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)

    # return all paths
    return filePaths
