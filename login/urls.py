from django.contrib import admin
from django.urls import path,include

import login
from login import views as api_views


urlpatterns = [
    path('go/',api_views.createUser,name='createUser')
]