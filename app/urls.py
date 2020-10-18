from django.urls import path
from .views import insert,update,delete,query,getRedis

urlpatterns = [
    # path('', index),
    # path('hello1/<str:name>/<int:age>', hello1),
    # path('hello2', hello2),
    path('insert', insert),
    path('update', update),
    path('delete', delete),
    path('query', query),
    path('getRedis', getRedis),
    # path('OO', OO.as_view()),
    # path('Temp', Temp.as_view()),
]
