from django.db import models

import random # for random data

USER = {
        'login': 'aleks',
        'email': 'aleks@mail.ru',
        'nick_name': 'aleks666',
        'avatar': '',
        'is_auth': False,
    }

QUESTIONS = [
    {
        'id': question_id,
        'like_count': random.randint(1, 100),
        'title': f'Quesion {question_id}',
        'text': f'Text of question {question_id}',
        'answers_count': random.randint(1, 10),
        'tags': [f'tag {i}' for i in range(random.randint(1, 10))],
        'answers': [],
    } for question_id in range(10)
]

for question in QUESTIONS:
    question['answers'] = [
        {
            'id': answer_id,
            'like_count': random.randint(1, 100),
            'text': f'Text of answer {answer_id}',
            'correct': random.choice([True, False]),
        } for answer_id in range(question['answers_count'])
    ]

TAGS = [f'Popular tag {tag_id}' for tag_id in range(random.randint(5, 10))]

BEST_USERS = [f'User {user_id}' for user_id in range(random.randint(2, 7))]
