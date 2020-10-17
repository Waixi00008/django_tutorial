"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import urls as app_urls
from get_by_douban import urls as douban_urls
from jinja_app import urls as jinja_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(app_urls)),
    path('douban/', include(douban_urls)),
    path('test/', include(jinja_urls)),
]
