from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>', views.question, name='question'),
    path('ask', views.ask, name='ask'),
    path('tag/<int:tag_id>', views.tag, name='tag'),
    path('login', views.login, name='login'),
    path('settings', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),
    path("logout", views.logout, name="logout"),
    path('hot', views.hot_questions, name='hot_questions'),
]
