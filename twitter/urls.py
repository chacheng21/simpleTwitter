"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from tweets import views as tweetViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', userViews.registerPage),
    path('login/', userViews.loginPage),
    path('logout/', userViews.logout, name='logout'),
    path('splash/', userViews.splashPage, name = 'splash'),
    path('', include('tweets.urls')),
    path('', include('tweets.urls'), name='user'),
    path('', include('tweets.urls'), name='hashtag')
]
