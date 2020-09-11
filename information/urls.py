
from django.urls import path, include
from information import views
from django import forms


app_name = 'information'

urlpatterns = [
    path('', views.index, name='index'),
    path('header/',views.header,name='header'),
    path('latestpost/',views.latestpost,name='latestpost'),
    path('page1/',views.page1,name='page1'),
    path('page2/',views.page2,name='page2'),
    path('page3/',views.page3,name='page3'),
    path('page4/',views.page4,name='page4'),
    path('page5/',views.page5,name='page5'),
    path('page6/',views.page6,name='page6'),
    path('aboutme/',views.aboutme,name='aboutme'),
]
