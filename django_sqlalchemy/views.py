from django.http import HttpResponse
from .sqlalchemy import db_session,User

def insert(request):
    user = User(name="waixi")
    db_session.add(user)
    db_session.commit()
    db_session.close()
    return HttpResponse('增')

def update(request):
    user = db_session.query(User).first()
    user.name="xiaobing"
    db_session.commit()
    return HttpResponse('改')

def delete(request):
    user = db_session.query(User).first()
    db_session.delete(user)
    db_session.commit()
    return HttpResponse('删')

def query(request):
    user = db_session.query(User).first()
    print(user)
    return HttpResponse('查')