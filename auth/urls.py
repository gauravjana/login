from django.contrib import admin
from django.urls import path,include

import login
from login import views as api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include(login.urls)),
    path('registerapi/',api_views.UserRegister.as_view(),name='registerapi'),
    path('loginapi/',api_views.UserLogin.as_view(),name='loginapi'),
    path('logout/',api_views.UserLogout.as_view(),name='logout'),


]