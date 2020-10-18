from django.urls import path
from .views import insert,update,delete,query

urlpatterns = [
    path('insert', insert),
    path('update', update),
    path('delete', delete),
    path('query', query),
]
