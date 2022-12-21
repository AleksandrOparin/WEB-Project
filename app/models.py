from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db.models import Sum, Count

from django.db.models.deletion import CASCADE


class QuestionManager(models.Manager):
    def top(self):
        return self.annotate(rating = Sum('votes__vote')).order_by('-rating')

    def new(self):
        return self.order_by('-pub_date')

    def tag(self, tag_id):
        tag = Tag.objects.get(id = tag_id)
        return tag.questions.annotate(rating = Sum('votes__vote')).order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    tags = models.ManyToManyField('Tag', related_name = 'questions')
    author = models.ForeignKey('Profile', models.CASCADE, related_name = 'questions')
    pub_date = models.DateTimeField(auto_now_add = True)
    votes = GenericRelation('Like', related_query_name = 'questions')

    objects = QuestionManager()

    def __str__(self):
        return self.title
    
    def get_tags(self):
        return self.tags.all()

    def get_text(self):
        return (self.text[:140] + '...') if len(self.text) > 160 else self.text

    def get_answers(self):
        return self.answers.all()

    def get_likes(self):
        return self.votes.sum_likes()


class AnswerManager(models.Manager):
    def ordered_answers(self, quest_id):
        return self.filter(question_id = quest_id).annotate(rating = Sum('votes__vote')).order_by('-correct').order_by('-rating')


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, models.CASCADE, related_name = 'answers')
    correct = models.BooleanField(default = False)
    author = models.ForeignKey('Profile', models.CASCADE, related_name = 'answers')
    pub_date = models.DateTimeField(auto_now_add = True)
    votes = GenericRelation('Like', related_name = 'answers')

    objects = AnswerManager()

    def __str__(self):
        return (self.text[:40] + '...')

    def get_likes(self):
        return self.votes.sum_likes()


class TagManager(models.Manager):
    def popular_tags(self):
        return self.annotate(raiting = Count('questions')).order_by('-raiting')[:10]


class Tag(models.Model):
    name = models.CharField(max_length = 30, unique=True)

    objects = TagManager()

    def __str__(self):
        return self.name


class ProfileManager(models.Manager):
    def top_profiles(self):
        return self.annotate(raiting = Count('questions')).order_by('-raiting')[:10]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    avatar = models.ImageField(null=True, blank = True, default='/static/img/default-avatar-icon.jpg', upload_to='avatar/%Y/%m/%d/')

    objects = ProfileManager()

    def __str__(self):
        return self.user.username


class LikeManager(models.Manager):
    use_for_related_fields = True

    def sum_likes(self):
        res = self.filter(vote__gt = 0).aggregate(Sum('vote')).get('vote__sum')
        if not res:
            res = 0
        return res

    def sum_rating(self):
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum')


class Like(models.Model):
    LIKE = 1
    NOTHING = 0
    DISLIKE = -1
 
    VOTES = (
        (LIKE, 'Like'),
        (NOTHING, 'Nothing'),
        (DISLIKE, 'Dislike')
    )
 
    vote = models.SmallIntegerField(choices = VOTES, default = NOTHING)
    user = models.ForeignKey('Profile', models.CASCADE, related_name = 'likes')
 
    content_type = models.ForeignKey(ContentType, models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeManager()
