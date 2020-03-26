def get_essay_question_ids(questions):
    essay_questions = filter(
        lambda q: (q.question_type == 'essay_question'),
        questions
    )

    only_ids = map(
        lambda q: (q.id),
        essay_questions
    )

    ids = []
    for id in only_ids:
        ids.append(id)

    return ids
