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

class Temp(View):
    def get(self,request):
        data = {
            'name': 'waixi',
            'title': 'django templates',
            'book': [
                {
                    "id":1,
                    "title":'书1',
                    "content":"内容1"
                },{
                    "id":2,
                    "title":'书2',
                    "content":"内容2"
                },{
                    "id":3,
                    "title":'书3',
                    "content":"内容3"
                },{
                    "id":4,
                    "title":'书4',
                    "content":"内容4"
                },{
                    "id":5,
                    "title":'书5',
                    "content":"内容5"
                },
            ],
            'list': []
        }

        return render(request,'index.html',data)