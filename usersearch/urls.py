from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from . import views

app_name = 'usersearch'
urlpatterns = [
    url(r'^search/', views.Search.as_view(), name='search'),

]