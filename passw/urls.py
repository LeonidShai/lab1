from django.urls import path
from passw.views import PasswView

urlpatterns = [
    path('', PasswView.as_view()),
]