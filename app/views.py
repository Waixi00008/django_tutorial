from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
# def index(request):
#     return HttpResponse('hello django')
#
# def hello1(request,name,age):
#     return HttpResponse('hello1 i am {0},age is {1}'.format(name,age))
#
# def hello2(request):
#     name = request.GET.get('name','')
#     age = request.GET.get('age',0)
#     return HttpResponse('hello2 i am {0},age is {1}'.format(name,age))

class OO(View):
    def get(self,request):
        return HttpResponse("hello 面向对象")