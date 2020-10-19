from django import forms
from django.forms import fields
from .models import Auth as AuthModel


class AuthModelForm(forms.ModelForm):
    class Meta:
        model = AuthModel
        #只把数据库的username和password做成表单form
        fields = ['username', 'password']  # '__all__'
        exclude = []  # 输入不专程表单字段的model字段
        # 一下都是自定义
        field_classes = {  # 定义字段的类型，一般会按照model的类型自动转换
            'username': forms.CharField,
            'password': forms.CharField
        }

        labels = {
            'username': '用户名',
            'password': '密码'
        }

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': '请输入用户名'}
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': '请输入密码'},
                render_value=True
            )
        }

        error_messages = {
            'username': {'required': '用户名不可以为空'},
            'password': {'min_length': '最爱哦不能低于10个字符'}
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) > 10:
            raise forms.ValidationError('用户名最大不可超过10')

        return username

class Auth(forms.Form):
    username = fields.CharField(label="用户名", max_length=18, widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}))
    password = fields.CharField(label="密码",required = False, widget=forms.TextInput(attrs={'placeholder': '请输入密码'}))
    email = fields.EmailField(label="邮箱",required = False, widget=forms.EmailInput(attrs={'placeholder': '请输入邮箱'}))

    # 可对当个进行验证
    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if not username:
            raise forms.ValidationError('用户名不可以为空！')

        if len(username) < 5:
            raise forms.ValidationError('用户名不能小于五个字符')

        if len(username) > 18:
            raise forms.ValidationError('用户名不能超过18')
        return username

    # 可对所有进行验证，出了一个错误下面的就不会报错了，所以使用该方法不好
    def clean(self):
        password = self.cleaned_data.get('password', '')
        if not password:
            raise forms.ValidationError('密码不可以为空！')
        if len(password) < 3:
            raise forms.ValidationError('密码不能小于5个字符')
        if len(password) > 8:
            raise forms.ValidationError('密码不能超过8个字符')

        email = self.cleaned_data.get('email', '')
        if not email:
            print(111)
            raise forms.ValidationError('邮箱不可以为空！')

