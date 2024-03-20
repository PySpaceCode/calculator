from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h1>This is my irst views</h1>")

def index(request):
    d1={
        "name":"rahul",
        "age":21
        }
    d1={"d1":d1}
    return render(request,"Rootapp/index.html",context={"d1":d1})

def show_dtl(request):
    a=20
    b=30
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    d1={"a":a,"b":b,"sum":sum,"sub":sub,"mul":mul,"div":div}
    return render(request,"Rootapp/dtl.html",context=d1)
def unknow(request):
    if request.method=="GET":
        #return HttpResponse("<h1>Get method will be used</h1>")
        return render(request,"rootapp/unknown.html")
    elif request.method=="POST":
        a=request.POST.get("a")
        b=int(request.POST.get("b"))
        d1={"a":a,"b":b}
        return render(request,"rootapp/unknown.html",context=d1)

    return render(request,"rootapp/unknown.html")

def  calculator(request):
    if request.method=="GET":
        return render(request,"Rootapp/calculator.html")
    elif request.method=="POST":
        if "btn_add" in request.POST:
            n1=int(request.POST.get("n1"))
            n2=int(request.POST.get("n2"))
            sum=n1+n2
            msg="Addition will be performed"
            d1={'sum':sum,"msg":msg}
            return render(request,"Rootapp/calculator.html",context=d1)
        elif "btn_sub" in request.POST:
            n1=int(request.POST.get("n1"))
            n2=int(request.POST.get("n2"))
            sum=n1-n2
            msg="Subtract will be performed"
            d1={'sum':sum,'msg':msg}
            return render(request,"Rootapp/calculator.html",context=d1)
        elif "btn_mul" in request.POST:
            n1=int(request.POST.get("n1"))
            n2=int(request.POST.get("n2"))
            sum=n1*n2
            msg="Multiply  will be performed"
            d1={'sum':sum,'msg':msg}
            return render(request,"Rootapp/calculator.html",context=d1)
        else:
            n1=int(request.POST.get("n1"))
            n2=int(request.POST.get("n2"))
            sum=n1/n2
            msg="Divide will be performed"
            d1={'sum':sum,'msg':msg}
            return render(request,"Rootapp/calculator.html",context=d1)

    return render(request,"Rootapp/calculator.html")

"""Task1 : Enter your fname,lname,username,email,password and print
   task2 :calculator by using django

"""