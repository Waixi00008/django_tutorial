from django.urls import path
from .views import index,hello1,hello2

urlpatterns = [
    path('', index),
    path('hello1/<str:name>/<int:age>', hello1),
    path('hello2', hello2)
]
