from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import Auth

class Register(View):
    TEMPLATE = 'register.html'

    def get(self, request):
        form = Auth()
        return render(request, self.TEMPLATE,{'form':form})

    def post(self,request):
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # print('username',username)
        # print('password',password)
        form = Auth(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print('username', username)
            print('password',password)
        return redirect('/form/register')