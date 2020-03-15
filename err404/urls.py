from django.urls import path
from err404.views import Err404View

urlpatterns = [
    path('', Err404View.as_view()),
]