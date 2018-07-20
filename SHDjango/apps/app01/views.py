'''
import re
import random

from django.http import HttpResponse
from django.views import View

from SHDjangolesson.settings import APIKEY
from .models import ArtsUser
from SHDjangolesson.note_check import YunPian




class ForCodeView(View):
    """获取手机验证码"""

    def post(self, request):
        mobile = request.POST.get('mobile', '')
        if mobile:
            # 验证是否为有效手机号
            mobile_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
            res = re.search(mobile_pat, mobile)
            if res:
                # 生成手机验证码
                code = ArtsUser()
                code.mobile = mobile
                c = random.randint(1000, 9999)
                code.code = str(c)
                code.save()
                code = ArtsUser.objects.filter(mobile=mobile).first().code
                yunpian = YunPian(APIKEY)
                sms_status = yunpian.send_sms(code=code, mobile=mobile)
                msg = sms_status.msg
                return HttpResponse(msg)
            else:
                msg = '请输入有效手机号码!'
                return HttpResponse(msg)
        else:
            msg = '手机号不能为空！'
            return HttpResponse(msg)

'''