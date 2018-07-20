from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name="用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name="联系地址")
    message = models.CharField(max_length=500, verbose_name="留言信息")
    create_time = models.DateTimeField(verbose_name=u"创建时间", default=timezone.now)

    class Meta:
        verbose_name = u"用户留言信息"
        verbose_name_plural = verbose_name
        db_table = "user_message"
        ordering = ["-create_time"]
