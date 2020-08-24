from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def view(request):
    name = request.GET[''] # 지역 값
    list1= request.GET[''] # 셀렉트 이름
    list2 = request.GET[''] # 셀렉트 이름
    

    return render(request,'view.html')

# def mycourse(request):




# def course (request):





