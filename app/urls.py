from django.urls import path
from .views import OO,Temp

urlpatterns = [
    # path('', index),
    # path('hello1/<str:name>/<int:age>', hello1),
    # path('hello2', hello2),
    path('OO', OO.as_view()),
    path('Temp', Temp.as_view()),
]
