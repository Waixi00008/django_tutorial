from django.urls import path
from .views import Music

urlpatterns = [
    path('music', Music.as_view()),
]
