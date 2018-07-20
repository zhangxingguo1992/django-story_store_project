from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Art,Tag
from django.db.models import Q


def SearchHandler(request):
    key = request.GET.get('key', '')    ##获取输入参数key对应的值，默认为空
    page = int(request.GET.get("page", 1))
    total = 0
    if key == '':
        return HttpResponseRedirect('/app/index')
    else:
        art_sets = Art.objects.filter(Q(a_title__contains=str(key))     # __contains  模糊查询，类似于数据中的 like bianry '% key %'
                                      | Q(a_info__contains=str(key))
                                      | Q(a_content__contains=str(key))).distinct() # distinct 去重
        total = art_sets.count()
        shownum = 10
        import math
        pagenum = int(math.ceil(total/shownum))
        context = dict(
            pagenum = pagenum,
            total = total,
            prev = 1,
            next = 1,
            pagerange = range(1,2),
            data = [],
            url = request.path,
            key = key ,
            page = 1
        )
        if page < 1:
            url = request.path + '?page=1&key=%s'%(key)
            return HttpResponseRedirect(url)
            # context.update(page = 1)
            # return render(request, 'home/search.html', context = context)

        if page > pagenum:
            context.update(page = 1)
            return render(request, 'home/search.html', context = context)

        offset = (page -1) * shownum
        data = art_sets[offset:offset + shownum]

        btnum = 5
        if btnum > pagenum:
            firstpage = 1
            lastpage = pagenum
        else:
            if page == 1:
                firstpage = 1
                lastpage = btnum
            else:
                firstpage = page - 3
                lastpage = page + btnum
                if firstpage < 1:
                    firstpage = 1
                if lastpage > pagenum:
                    lastpage = pagenum
        prev = page - 1
        next = page + 1

        if prev < 1:
            prev = 1
        if next > pagenum:
            next = pagenum

        context = dict(
            pagenum=pagenum,
            total=total,
            prev=prev,
            next=next,
            pagerange=range(firstpage, lastpage + 1),
            data=data,
            url=request.path,
            page=page,
            key = key
        )

        return render(request, 'home/search.html', context=context)