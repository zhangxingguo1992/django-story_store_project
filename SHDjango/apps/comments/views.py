from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,get_object_or_404,redirect

from app01.models import Art,ArtsUser
from comments.models import Comment
from comments.forms import CommentForm
from SHDjangolesson import utils

def art_comment(request,art_pk):
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    art = get_object_or_404(Art,pk = art_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.art = art
            comment.save()
            comment_list = art.comment_set.all()
            context = {
                'art':art,
                'form':form,
                'comment_list':comment_list,
                'comment_count':len(comment_list),
            }
            return render(request,'home/detail.html',context = context)
        else:
            comment_list = art.comment_set.all()
            context = {
                'art':art,
                'form': form,
                'comment_list': comment_list,
                'comment_count': len(comment_list),
            }
            utils.flash(request,'error',f'用户登录失败')
            return render(request,'home/detail.html',context=context)
    return redirect(art)