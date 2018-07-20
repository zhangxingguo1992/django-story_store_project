# import requests  # 需要先pip install requests
# class YunPian(object):
#     def __init__(self,api_key):
#         self.api_key = api_key
#         self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'
#     def send_sms(self,code,mobile):
#         parmas = {
#             'apikey':self.api_key,
#             'mobile':mobile,
#             'text':'【章兴国】正在进行登录操作，您的验证码是#code#'.format(code=code)
#         }
#         # text必须要跟云片后台的模板内容 保持一致，不然发送不出去！
#         r = requests.post(self.single_send_url,data = parmas)
#         print(r)
#
# if __name__ == '__main__':
#     pass