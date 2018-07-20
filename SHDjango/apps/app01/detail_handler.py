from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Art,Tag,Chapter
from comments.models import Comment
from comments.forms import CommentForm



def DetailHandler(request):

    article_id = request.GET.get('id', None)
    if article_id == None:
        return HttpResponseRedirect('/app/index.html')
    else:
        art = Art.objects.get(id = int(article_id))

        # 评论信息
        form = CommentForm()
        comment_list = Comment.objects.filter(art = article_id)
        # 获取章节
        art_capters = Chapter.objects.filter(art=article_id)


        # import redis
        # r = redis.Redis()
        # visit = 'a'+str(article_id)
        # res = r.get(visit)
        # if res == None:
        #     r.set(visit,0)
        # r.incr(visit)
        # time_visit = r.get(visit)




        context = {'art':art,
                   'form':form,
                   'comment_list':comment_list,
                   'comment_count':len(comment_list),
                   'art_capters':art_capters,
                   # 'time_visit':time_visit
                   }
        return render(request, 'home/detail.html', context = context)
#
# # 小说章节
def ArtCapterHandler(request):
    capter_id = int(request.GET.get('id',0))
    if capter_id == 0:
        return DetailHandler(request)
    art_capter = Chapter.objects.get(id = capter_id)
    context = dict(
        art_capter = art_capter
    )
    return render(request,'home/capter_handler.html',context=context)