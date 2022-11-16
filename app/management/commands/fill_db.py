from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

import random
from faker import Faker

from app.models import Question, Answer, Tag, Profile, Like


# For multiplying on ration
USER_COUNT = 1
TAGS_COUNT = 1
QUESTIONS_COUNT = 10
ANSWERS_COUNT = 100
VOTES_COUNT = 200


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faker = Faker()


    def add_arguments(self, parser):
        parser.add_argument('--ratio')


    def create_users_and_profiles(self, count : int):
        print("Start profiles generating")
        users = []
        profiles = []

        for i in range(count):
            username = self.faker.user_name()
            email = self.faker.email()
            password = self.faker.password()
            avatar = f'/app/DBImages/test-avatar-{random.randint(1, 6)}.jpg'

            user = User(username=username, email=email, password=password)
            profile = Profile(avatar=avatar)

            users.append(user)
            profiles.append(profile)

        User.objects.bulk_create(users)
        Profile.objects.bulk_create(profiles)
        print("End profiles generating")


    def create_tags(self, count : int):
        print("Start tags generating")

        tags = [Tag(name = self.faker.word()) for i in range(count)]
        Tag.objects.bulk_create(tags)

        print("End tags generating")


    def create_questions(self, count : int):
        print("Start questions generating")
        profiles = Profile.objects.all()

        questions = [Question
                (
                    title=self.faker.paragraph(1)[:-1] + '?',
                    text=self.faker.paragraph(random.randint(4, 10)),
                    author=random.choice(profiles)
                ) for i in range(count)
            ]
        questions = Question.objects.bulk_create(questions)

        tags = []
        for i in range(count):
            tags_count = random.randint(1, 6)
            for j in range(tags_count):
                tags.append(random.choice(Tag.objects.all()))
            questions[i].tags.add(*tags[:n_tags])

        print("End questions generating")


    def create_answers(self, cout : int):
        print("Start answers generating")
        questions = Question.objects.all()
        profiles = Profile.objects.all()

        answers = [Answer
            (
                text=self.faker.paragraph(random.randint(4, 10)),
                question=random.choice(questions),
                author=random.choice(profiles),
            ) for i in range(count)
        ]

        Answer.objects.bulk_create(answers)
        print("End answers generating")


    def create_questions_likes(self, cout : int):
        print("Start Qlikes generating")
        profiles = Profile.objects.all()

        questions_ids = Question.objects.values_list('id', flat=True)
        qtype = ContentType.objects.get_for_model(Question)

        qlikes = [Like(content_type = qtype, vote = 1, user = random.choice(profiles), object_id = random.choice(questions_ids)) for i in range(count)]

        Like.objects.bulk_create(qlikes)
        print("End Qlikes generating")


    def create_answers_likes(self, count : int):
        print("Start Alikes generating")
        profiles = Profile.objects.all()

        answers_ids = Answer.objects.values_list('id', flat=True)
        atype = ContentType.objects.get_for_model(Answer)

        alikes = [Like(content_type = atype, vote = 1, user = random.choice(profiles), object_id = random.choice(answers_ids)) for i in range(count)]

        Like.objects.bulk_create(alikes)

        print("End Alikes generating")


    def handle(self, *args, **options):
        retio = None
        # if options['ratio']
        #     ratio = int(options['ratio'])
        # else 
        #     ratio = 10000

        ratio = 1

        self.create_users_and_profiles(ratio * USER_COUNT)
        # self.create_tags(ratio * TAGS_COUNT)
        # self.create_questions(ratio * QUESTIONS_COUNT)
        # self.create_answers(ratio * ANSWERS_COUNT)
        # self.create_questions_likes(ratio * VOTES_COUNT / 2)
        # self.create_answers_likes(ratio * VOTES_COUNT / 2)