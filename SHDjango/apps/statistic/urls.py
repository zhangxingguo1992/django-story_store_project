
from django.conf.urls import url
from .views import render_index
from .statistic_handler import HistogramHandler
from .statistic_piehandler import PieHandler
# from .ca_user import tag_show

urlpatterns = [
	url(r'^index/$', render_index),
	url(r'^statics/$', HistogramHandler),
	url(r'^pie/$', PieHandler)
]
