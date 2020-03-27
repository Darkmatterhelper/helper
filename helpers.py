import pandas as pd
import requests
import json
import io


def get_essay_question_ids(questions):
    essay_questions = filter(
        lambda q: (q.question_type == 'essay_question'),
        questions
    )

    only_ids = map(
        lambda q: (str(q.id)),
        essay_questions
    )

    ids = []
    for id in only_ids:
        ids.append(id)

    return ids


def create_quiz_report(base_url, auth_header, course_id, quiz_id, report_type):
    url = f'{base_url}/api/v1/courses/{str(course_id)}/quizzes/{str(quiz_id)}/reports'

    payload = {"quiz_report[report_type]": report_type,
               "quiz_report[includes_all_versions]": True}

    r = requests.post(url, headers=auth_header, data=payload)

    export_details = json.loads(r.text)

    return(export_details)


def get_progress(progress_url, auth_header):
    r_progress = requests.get(progress_url, headers=auth_header)
    progress_state = json.loads(r_progress.text)
    progress_completion = progress_state['workflow_state']
    return(progress_completion)


def download_quiz_report(report_info, auth_header):
    # downloads the quiz reports and gathers info
    try:
        download_url = report_info['file']['url']
        filename = report_info['file']['display_name']
        res = requests.get(download_url, headers=auth_header)

        with (open('raw_reports/' + filename, 'wb')) as output:
            output.write(res.content)
            print(f'Creating Raw Report: {filename}')

        df = pd.read_csv(io.StringIO(res.content.decode('utf-8')))

        return df
    except:
        print('ERROR: There was a problem downloading the quiz report')
        print('...if a quiz has just changed or submission just added, please try again in a moment')
        exit()
