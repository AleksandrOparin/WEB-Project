from django.db import models

# for random data
import random
# print(random.randint(0, 9))

QUESTIONS = [
    {
        'id': question_id,
        'like_count': random.randint(1, 100),
        'title': f'Quesion {question_id}',
        'text': f'Text of question {question_id}',
        'answers_count': random.randint(1, 10),
        'tags': ['tag' for i in range(random.randint(1, 10))],
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

TAGS = [f'Popular tag {i}' for i in range(random.randint(5, 10))]
