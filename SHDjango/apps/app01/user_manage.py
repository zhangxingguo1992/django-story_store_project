from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from app01 import forms
from app01 import models
from django.views.decorators.csrf import csrf_exempt
from SHDjangolesson import utils,check_code
from io import BytesIO

def create_pwd_md5(str_pwd):
    import hashlib
    h1 = hashlib.md5()
    h1.update(str_pwd.encode(encoding = 'utf-8'))
    return h1.hexdigest()

# 用户注册功能
@csrf_exempt
def RegisterHandler(request):
    userform = forms.ArtsUserRegForm()
    if request.method == 'POST':
        userform = forms.ArtsUserRegForm(data = request.POST)
        if not userform.is_valid():
            utils.flash(request,'error',f'用户注册失败')
            context = dict(
                form = forms.ArtsUserRegForm(data=request.POST)
            )
            return render(request,'home/register_handler.html',context=context)
        username = userform.cleaned_data['username']     #cleaned_data 就是读取表单返回的值，返回类型为字典dict型
        password = create_pwd_md5(userform.cleaned_data['password'])
        email = userform.cleaned_data['email']
        art_user = models.ArtsUser(username=username,password=password,email=email)
        art_user.save()
        utils.flash(request,'success',f'恭喜，注册用户{username}成功！')
    context = dict(
        form = userform
    )
    return render(request,'home/register_handler.html',context=context)


# 会员登录功能
@csrf_exempt
def LoginHandler(request):
    userform = forms.ArtsUserLoginForm()
    if request.method == 'POST':
        userform = forms.ArtsUserLoginForm(data=request.POST)
        if not userform.is_valid():
            utils.flash(request,'error',f'用户登录失败')
            context = dict(form = userform)
            return render(request,'home/login_handler.html',context=context)
        # username = userform.cleaned_data['username']
        # password = create_pwd_md5(userform.cleaned_data['password'])
        post_check_code = request.POST.get('check_code')
        session_check_code = request.session['check_code']
        # user = models.ArtsUser.objects.filter(username__exact=username,  # 加了__exact代表名称严格等于 "username" 的人
        #                                       password__exact=password).first()   # 如果是__iexact 表示不区分大小写
        if post_check_code.lower() == session_check_code.lower():
            username = userform.cleaned_data['username']
            password = create_pwd_md5(userform.cleaned_data['password'])
            user = models.ArtsUser.objects.filter(username__exact=username,  # 加了__exact代表名称严格等于 "username" 的人
                                                  password__exact=password).first()
            if user:
                request.session['muser'] = user
                request.session['check_code'] = post_check_code
                return HttpResponseRedirect('/app/index/')
            else:
                utils.flash(request,'error',f'用户{username}登录失败')
        else:
            utils.flash(request, 'error', f'请输入正确的验证码！')

    context = dict(form = userform)
    return render(request,'home/login_handler.html',context=context)


def LogoutHandler(request):
    del request.session['muser']
    return HttpResponseRedirect('/app/login/')

def create_code_img(request):
    f = BytesIO()   #直接在内存开辟一点空间存放临时生成的图片
    img,code = check_code.create_validate_code()
    request.session['check_code'] = code
    img.save(f,'PNG')   #生成的图片放置于开辟的内存中
    return HttpResponse(f.getvalue())   #将内存的数据读取出来，并以HttpResponse返回