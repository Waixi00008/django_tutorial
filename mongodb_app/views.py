from django.http import HttpResponse
# from .models import User
from django.conf import settings

db = settings.DB

def insert(request):
    db.user.insert({'name': 'zhaos', 'age': 23,'www':1});
    return HttpResponse('增')

def update(request):
    db.user.update({'name': 'zhaos'}, {'$set': {'name': 'waixi'}})
    return HttpResponse('改')

def delete(request):
    db.user.remove({'name': 'waixi'})
    return HttpResponse('删')

def query(request):
    users=db.user.find()
    print(users)
    return HttpResponse('查')