import random
import time
from django.shortcuts import HttpResponseRedirect,HttpResponse
from functools import wraps
from django.contrib import messages

# 校验用户登录否，session是否有数据
def check_user_login(func):
    @wraps(func)
    def _wrapper(*args,**kwargs):
        request = args[0]
        if not request.session.has_key('muser'):
            return HttpResponseRedirect('/app/login')
        return func(*args,**kwargs)
    return _wrapper


'''
django后台向前端发送一个闪存消息
利用django自带的message系统发送一个闪存消息
'''
def flash(request,title,text,level='info'):
    LEVEL_MAP = {
        'info':messages.INFO,
        'debug':messages.DEBUG,
        'success':messages.SUCCESS,
        'warning':messages.WARNING,
        'error':messages.ERROR
    }
    level = LEVEL_MAP[level]
    messages.add_message(request,level,text,title)
    return HttpResponse(text)


# 产生订单号
def create_order_id():
    order_id = '%s%s' % (int(time.time()), random.randint(10,100))
    return order_id