from django.shortcuts import render,redirect
from django.views.generic import View


class Register(View):
    TEMPLATE = 'register.html'

    def get(self, request):
        return render(request, self.TEMPLATE)

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username',username)
        print('password',password)
        return redirect('/form/register')