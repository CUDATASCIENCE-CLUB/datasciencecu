from django.urls import path,include
from . import views
from django.conf.urls import url
urlpatterns = [
    path('eventblogs/', views.ev, name='ev'),
    path('blogdetail', views.blogdetail, name='blogpage'),
    path('discussion', views.discussion, name='discussion'),
    path('newcomment', views.newcomment, name='newcomment'),
    path('threads', views.discussion_list, name='threads'),
    path('question', views.Question, name='question'),

]
