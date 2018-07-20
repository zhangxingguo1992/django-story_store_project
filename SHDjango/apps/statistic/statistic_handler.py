from django.shortcuts import render
from app01.models import Art,Tag


def HistogramHandler(request):
   lx = []
   ly = []
   tag = Tag.objects.values('id', 't_name')
   for t in tag:
       lx.append(t.get('t_name'))
       art_num = Art.objects.filter(a_tag_id=t.get('id')).count()
       ly.append(art_num)

   import json
   myjson = {
      'type': 'column',
      'colorByPoint': 'true',
      'data': ly,
      'showInLegend': 'true'
   }
   mxjson = {
      'categories':lx
   }

   datay = json.dumps(myjson)
   datax = json.dumps(mxjson)
   # locals()返回的字典对所有局部变量的名称与值进行映射
   return render(request, "statics.html", locals())

