from django.conf.urls import url
from .views import MessageSubmit

urlpatterns = [
    url(r'^$',  MessageSubmit, name='go_form'),
















]