"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import Http404
from django.shortcuts import render
from django.urls import path
from .fake_db import user_db

def user_list(request):
    names_list = [{'id': key, 'name': value['이름']} for key, value in user_db.items()]
    return render(request, 'user_list.html', {'data':names_list})

def user_info(request, user_id):
    if user_id > len(user_db):
        raise Http404('유저를 찾을 수 없어요!')
    info = user_db[user_id]
    return render(request, 'user_info.html', {'data':info})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', user_list),
    # user_info.html에서 URL 패턴으로 접근 할 수 있도록 name 속성 사용!
    path('users/<int:user_id>/', user_info, name='user_info'),
]
