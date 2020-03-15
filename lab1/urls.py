"""lab1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.http import HttpResponse
from django.shortcuts import render

import datetime

def current_time(request):
    now = datetime.datetime.now()
    html = f"<html><body>Now, time is: {now}</body></html>"
    return HttpResponse(html)

def current_handler404(request, exception):
    return HttpResponse("<html><body>This page not found. Error 404!<br>Pages only: login, passw, parolo, time</html></body>", status=404)

def e_hand404(request, exception):
    return render(request, 'err404/index.html')

handler404 = e_hand404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time', current_time),
    path('login/', include('login.urls')),
    path('parolo/', include('parolo.urls')),
    path('passw/', include('passw.urls')),
    path('err404/', include('err404.urls'))
]
