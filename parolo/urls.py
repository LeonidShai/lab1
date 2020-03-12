from django.urls import path
from parolo.views import ParoloView

urlpatterns = [
    path('', ParoloView.as_view()),
]