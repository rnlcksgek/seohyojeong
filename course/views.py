from django.shortcuts import render
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')

def view(request):
    if request.user.is_anonymous:
        return render(request,'home.html')
    name = request.GET[''] # 지역 값
    list1= request.GET[''] # 셀렉트 이름
    list2 = request.GET[''] # 셀렉트 이름
    #if 경로 포함:
        #obj = model.objects.filter(Q("dbname in name") & Q("dblist1 = list1") & Q("dblist2 = list2"))
    #else:
        #obj = model.objects.filter(Q("dbname = name ") & Q("dblist1 = list1") & Q("dblist2 = list2"))
    return render(request,'view.html',{"courseList" : obj})
def mycourse(request):
    if request.user.is_anonymous:
        return render(request,'home.html')
    obj = model.objects.filter(Q("dbuser = request.user"))
    return render(request,'mycourse.html')

def detail (request,id):
    # obj = model.objects.filter(Q("dbid = id"))
    return render(request, 'detail.html', {"details" : obj})








