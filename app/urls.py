from django.conf import settings
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>', views.question, name='question'),
    path('ask', views.ask, name='ask'),
    path('tag/<int:tag_id>', views.tag, name='tag'),
    path('login', views.login, name='login'),
    path('settings', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name="logout"),
    path('hot', views.hot_questions, name='hot_questions'),
    path('likequestion/', views.like_question, name='like_question'),
    path('dislikequestion/', views.dislike_question, name='dislike_question'),
    path('likeanswer/', views.like_answer, name='like_answer'),
    path('dislikeanswer/', views.dislike_answer, name='dislike_answer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
