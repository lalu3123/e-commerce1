from django.shortcuts import render,redirect
from .models import user,prd
# Create your views here.

def log(request):
    return render(request,'login.html')


def reg(request):
    return render(request,'reg.html')

def hom(request):
    data=prd.objects.all()
    for i in data:
        print(i.prd_name)
    return render(request, 'home.html',{'data':data})

def log_btn(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if request.method == "POST":
        name = request.POST.get('name')
        pas = request.POST.get('pass')
        print(name)
        print(pas)
        if user.objects.filter(name=name, password=pas).exists():
            return redirect('home')
        else:return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pas = request.POST.get('pass')
        em = request.POST.get('email')
        ph = request.POST.get('ph')
        add = request.POST.get('add')
        user.objects.create(name=name, password=pas,Email=em,ph=ph,add=add)
        return redirect('login')
        print(name)
    return render(request, 'reg.html')
