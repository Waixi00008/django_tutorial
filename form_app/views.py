from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .forms import Auth,AuthModelForm
from .models import Auth as AuthModel

class Register(View):
    TEMPLATE = 'register.html'

    def get(self, request):
        # form = Auth()
        # 从数据库读取
        user = AuthModel.objects.filter(pk=1).first()

        if user:
            form = AuthModelForm(instance=user)
        else:
            form = AuthModelForm()
        return render(request, self.TEMPLATE,{'form':form})

    def post(self,request):
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # print('username',username)
        # print('password',password)

        # form = Auth(request.POST)
        form = AuthModelForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # email = form.cleaned_data.get('email')
            print('username', username)
            print('password',password)
            # print('email',email)
            form.save()
        else:
            # 验证有错时
            return render(request, self.TEMPLATE, {'form': form})
        return redirect(reverse('register'))