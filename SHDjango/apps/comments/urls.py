from django.conf.urls import url
from comments import views
app_name = 'comments'

urlpatterns = [
    url(r'^app/(?P<art_pk>[0-9]+)/$', views.art_comment, name='art_comment'),


]