from django.shortcuts import render,redirect,reverse
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
            email = form.cleaned_data.get('email')
            print('username', username)
            print('password',password)
            print('email',email)
        else:
            # 验证有错时
            return render(request, self.TEMPLATE, {'form': form})
        return redirect(reverse('register'))