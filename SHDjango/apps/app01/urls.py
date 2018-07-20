from django.conf.urls import url
# from app01.views import ForCodeView
from app01.index_handler import indexHandLer
from app01.search_handler import SearchHandler
from app01.detail_handler import DetailHandler,ArtCapterHandler
from app01.user_manage import RegisterHandler,LoginHandler,LogoutHandler,create_code_img
from app01 import cart_handler

urlpatterns = [

    url(r'^index/$', indexHandLer),
    url(r'^search/$', SearchHandler),
    url(r'^detail/$', DetailHandler),
    url(r'^register/$', RegisterHandler,name='user_register'),
    url(r'^login/$', LoginHandler,name='user_login'),
    url(r'^logout/$', LogoutHandler,name='user_logout'),
    url(r'^cart/view/$', cart_handler.ViewCartHandler),
    url(r'^cart/add/$', cart_handler.AddCartHandler),
    url(r'^cart/clean/$', cart_handler.CleanCartHandler),
	url(r'^cart/order/$', cart_handler.CartOrderHandler),
    url(r'^capter/$', ArtCapterHandler),
    url(r'^create_code_img/$', create_code_img),
    url(r'^cart/submit_order/$',cart_handler.OrderSubmitHandler,name='product_order'),
    # url(r'^forcode/$', ForCodeView.as_view(),name='forcode'),

]