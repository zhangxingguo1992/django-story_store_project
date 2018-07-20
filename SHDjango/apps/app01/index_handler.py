from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Art,Tag
# import logging
# from SHDjangolesson.settings import logger
'''
接口URL： / art / index?page = 1 & t = 1

方法：GET

输入参数说明：
page: 第几页
t: 标签类别，整数标识
    eg: 0 - -全部
    1 - -爱情小说
    2—科幻小说

输出：
    渲染首页卡片式页面
'''

def indexHandLer(request):
    url = request.path
    page = int(request.GET.get('page', 1)) # 如果没有给page值，默认为 1  ，所在页码
    t = int(request.GET.get('t', 0))   # 所在标签类，0代表全部标签
    total = 0   # 初始化总量，默认有0本书
    tags = Tag.objects.filter(t_flag = 0)  # 所有的标签对象
    # 计算查询的记录条数
    if t == 0:
        art_set = Art.objects.filter(a_flag = 0)   # queryset  文章集合
        total = art_set.count()     # 文章数量
    else:
        tag_id = t
        art_set = Art.objects.filter(a_flag = 0,a_tag_id=tag_id)
        total = art_set.count()


    #
    # import redis
    # r =  redis.Redis()
    # res = r.get('visit')
    # if res == None:
    #     r.set('visit',0)
    # r.incr('visit')
    # time_visit = r.get('visit')



    # 初始化页面
    context = dict(
        pagenum = 1,
        total = 0,
        prev = 1,
        next = 1,
        pagerange = range(1,2),
        data = [],   # 显示当前页面文章的内容
        url = request.path,
        tags = tags,
        page = 1,
        t = 0,
        # time_visit = time_visit
    )
    # logger.info("IndexHandler request Handler begin")
    shownum = 12  # 每页显示12条信息
    if total>0:
        import math
        pagenum = math.ceil(total / shownum)
        if page < 1:
            url = request.path + '?page=1&t=0'
            return HttpResponseRedirect(url)  # 重定向
        if page>pagenum:
            url = request.path + '?page=%s&t=%s' % (pagenum, t)
            return HttpResponseRedirect(url)
        offset = (page-1) * shownum
        if t == 0:
            data = Art.objects.all()[offset:shownum+offset]
        else:
            data = Art.objects.filter(a_tag_id = t)[offset:shownum+offset]

        btnum = 5
        if btnum > pagenum:
            firstpage = 1
            lastpage = pagenum
        else:
            if page == 1:
                firstpage = 1
                lastpage = btnum
            else:
                firstpage = page -3
                lastpage = page + btnum
                if firstpage < 1:
                    firstpage = 1
                if lastpage > pagenum:
                    lastpage = pagenum
        prev = page - 1  # 上一页
        next = page + 1   # 下一页

        if prev < 1:
            prev = 1
        if next > pagenum:
            next = pagenum

        context = dict(
            pagenum = pagenum,
            total = total,
            prev = prev,
            next = next,
            pagerange = range(firstpage,lastpage+1),
            data = data,
            url = request.path,
            tags = tags,
            page = page,
            t = t,
            # time_visit=time_visit

        )

    return render(request, 'home/index.html', context=context)



