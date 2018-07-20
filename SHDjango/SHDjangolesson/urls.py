"""SHDjangolesson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from app01.views import hello_world
from statistic.views import render_index
import xadmin
from django.views.generic.base import RedirectView

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^app/', include('app01.urls')),
    url(r'^message/', include('message.urls')),
    url(r'^shtml/', include('statistic.urls')),
# url(r'^account/', include('account.urls', namespace='account', app_name='account')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^comments/', include("comments.urls")),
    url(r'^$',RedirectView.as_view(url='/app/index/')),
]
