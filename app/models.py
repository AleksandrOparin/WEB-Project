from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db.models import Sum, Count

from django.db.models.deletion import CASCADE

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='questions')
    author = models.ForeignKey('Profile', models.CASCADE, related_name='questions')
    pub_date = models.DateTimeField(auto_now_add=True)
    votes = GenericRelation('Like', related_query_name='questions')

    # def __str__(self):
    #     return self.title

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, models.CASCADE, related_name='answers')
    correct = models.BooleanField(default=False)
    author = models.ForeignKey('Profile', models.CASCADE, related_name='answers')
    pub_date = models.DateTimeField(auto_now_add=True)
    votes = GenericRelation('Like', related_name='answers')

    # def __str__(self):
    #     return (self.text[:40] + '...')

class Tag(models.Model):
    name = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.name

class Profile(models.Model):
    avatar = models.ImageField(blank = True, upload_to = "DBImages/")
    user = models.OneToOneField(User, models.CASCADE)

    # def __str__(self):
    #     return self.user.username

class Like(models.Model):
    LIKE = 1
    NOTHING = 0
    DISLIKE = -1
 
    VOTES = (
        (LIKE, 'Like'),
        (NOTHING, 'Nothing'),
        (DISLIKE, 'Dislike')
    )
 
    vote = models.SmallIntegerField(choices=VOTES, default=NOTHING)
    user = models.ForeignKey('Profile', models.CASCADE, related_name='likes')
 
    content_type = models.ForeignKey(ContentType, models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


# import random # for random data

# USER = {
#         'login': 'aleks',
#         'email': 'aleks@mail.ru',
#         'nick_name': 'aleks666',
#         'avatar': '',
#         'is_auth': False,
#     }

# QUESTIONS = [
#     {
#         'id': question_id,
#         'like_count': random.randint(1, 100),
#         'title': f'Quesion {question_id}',
#         'text': f'Text of question {question_id}',
#         'answers_count': random.randint(1, 10),
#         'tags': [f'tag {i}' for i in range(random.randint(1, 10))],
#         'answers': [],
#     } for question_id in range(10)
# ]

# for question in QUESTIONS:
#     question['answers'] = [
#         {
#             'id': answer_id,
#             'like_count': random.randint(1, 100),
#             'text': f'Text of answer {answer_id}',
#             'correct': random.choice([True, False]),
#         } for answer_id in range(question['answers_count'])
#     ]

# TAGS = [f'Popular tag {tag_id}' for tag_id in range(random.randint(5, 10))]

# BEST_USERS = [f'User {user_id}' for user_id in range(random.randint(2, 7))]
