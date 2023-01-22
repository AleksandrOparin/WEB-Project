from django import template 
from app import models
from django.contrib.contenttypes.models import ContentType

register = template.Library()

# For question
@register.filter(name = 'isQuestionLikeUp')
def is_question_like_up(question, profile):    
    return models.Like.objects.filter(content_type = ContentType.objects.get_for_model(models.Question), 
    vote = 1, user = profile, object_id = question.id)

@register.filter(name = 'isQuestionLikeDown')
def is_question_like_down(question, profile):
    return models.Like.objects.filter(content_type = ContentType.objects.get_for_model(models.Question), 
    vote = -1, user = profile, object_id = question.id)

# For answer
@register.filter(name = 'isAnswerLikeUp')
def is_answer_like_up(answer, profile):
    return models.Like.objects.filter(content_type = ContentType.objects.get_for_model(models.Answer), 
    vote = 1, user = profile, object_id = answer.id)

@register.filter(name = 'isAnswerLikeDown')
def is_answer_like_down(answer, profile):
    return models.Like.objects.filter(content_type = ContentType.objects.get_for_model(models.Answer), 
    vote = -1, user = profile, object_id = answer.id)