from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from app.models import Question, Answer, Tag, Profile, Like


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Question.objects.all().delete()
        Answer.objects.all().delete()
        Tag.objects.all().delete()
        Like.objects.all().delete()