from django import forms
from django.forms import widgets
from SHDjangolesson.settings import SEX_CHOICES,FLAGS_CHOICES,PAY_CHOICES
from app01 import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# 会员注册表单
class ArtsUserRegForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        required=True,
        min_length=3,
        max_length=50,
        widget=widgets.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'请输入用户名，长度为3~50',
            }),
        error_messages={
            'required':'对不起，用户名不能为空！',
            'min_length':'不行，长度小于3',
            'max_length':'sorry,长度太长，大于50',
        }
    )
    password = forms.CharField(
        label='密码',
        required=True,
        min_length=6,
        max_length=20,
        widget=widgets.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'请输入密码，长度为6~20',
            }
        ),
        # validators=[RegexValidator(r'((?=.*\d))^.{6,12}$','必须包含数字'),
        #             RegexValidator(r'((?=.*[a-zA-Z]))^.{1,6}$','必须包含字母')],
        error_messages={
            'required':'对不起，密码不能为空！',
            'min_length':'不行，长度小于6',
            'max_length':'sorry,长度太长，大于20',
        }
    )
    pwd_again = forms.CharField(
        label='确认密码',
        # render_value会对于PasswordInput，错误是否清空密码输入框内容，默认为清除
        widget = widgets.PasswordInput(
            attrs={'class':'form-control','placeholder':'请再次输入密码！'},
            render_value=True
        ),
        required = True,
        strip=True,
        error_messages={'required':'请再次确认密码！',}
    )
    telephonenum = forms.CharField(
        label='手机号码',
        widget = widgets.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入手机号码',
            }
        ),
        error_messages={
            'required': '对不起，手机不能为空！',
            'max_length': 'sorry,长度太长，大于13',
        }
    )
    email = forms.EmailField(
        label='邮箱',
        required=True,
        widget=widgets.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'请输入邮箱',
            }
        ),
        error_messages={
            'required':'对不起，邮箱不能为空！',
            'invalid':'请输入正确的邮箱格式',
        }
    )


    def clean_username(self):
        # 对username字段进行扩展校验
        username = self.cleaned_data.get('username','')
        users = models.ArtsUser.objects.filter(username=username).count()
        if users:
            raise ValidationError('用户已经存在')
        return username

    def clean_email(self):
        # 对email字段进行校验
        email = self.cleaned_data.get('email','')
        users = models.ArtsUser.objects.filter(email = email).count()
        if users:
            raise ValidationError('邮箱已经存在')
        return email
    def _clean_new_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('pwd_again')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError('两次密码不匹配！')
    def clean(self):
        # 是基于form对象的验证，字段全部验证通过会调用clean函数进行验证
        self._clean_new_password2()


# 会员登录表单
class ArtsUserLoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        required=True,
        min_length=3,
        max_length=50,
        widget=widgets.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'请输入用户名，长度为3~50',
            }
        ),
        error_messages={
            'required':'对不起，用户名不能为空！',
            'min_length':'不行，长度小于3',
            'max_length':'sorry,长度太长，大于50',
        }
    )
    password = forms.CharField(
        label='密码',
        required=True,
        min_length=6,
        max_length=20,
        widget=widgets.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'请输入密码，长度为6~20',
            }
        ),
        error_messages={
            'required':'对不起，密码不能为空！',
            'min_length':'不行，长度小于6',
            'max_length':'sorry,长度太长，大于20',
        }
    )




'''
订单表单
'''
class OrderForms(forms.Form):
    address =  forms.CharField(
		label="配送地址",
		required=True,
		widget=widgets.TextInput(
			attrs={
				"class": "form-control",
				"placeholder": "请输入配送地址",
			}),
		error_messages={
			"required": "对不起，配送地址不能为空！",
		}
	)
    pay_type = forms.ChoiceField(
		label="支付方式",
		required=True,
		choices=PAY_CHOICES,
		widget=forms.RadioSelect()
	)
    phone = forms.CharField(
		label="手机",
		required=True,
		widget=widgets.TextInput(
			attrs={
				"class": "form-control",
				"placeholder": "请输入手机",
			}),
		error_messages={
			"required": "对不起，手机不能为空！",
		}
	)
