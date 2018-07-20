from django.db import models

from django.utils import timezone
from SHDjangolesson.settings import SEX_CHOICES,FLAGS_CHOICES

# python_2_unicode_compatible 装饰器用于兼容 Python2
from django.utils.six import python_2_unicode_compatible
from app01.models import Art,ArtsUser

@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100,verbose_name='评论者')
    title = models.CharField(max_length=255,verbose_name='评论标题')
    text = models.TextField(verbose_name='评论内容')
    created_time = models.DateTimeField(default=timezone.now,db_index=True,
                                        verbose_name='添加时间')
    art = models.ForeignKey(Art,verbose_name='评论的文章')
    flag = models.IntegerField(default=0,verbose_name='控制字段',choices=FLAGS_CHOICES)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'comments'
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
