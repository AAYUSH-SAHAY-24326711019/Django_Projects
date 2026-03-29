from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About response")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydictionary = {
        "name" : name,
        "age"  : age
    }
    return JsonResponse(mydictionary)

def myfirstpage(request):
    return render(request,"index.html")

def mythirdpage(request):
    var = "Hello World (new string)"
    greeting = "Hello, How are you ? "
    fruits = ['apple','mango','banana']

    num1 , num2 = 13,5
    ans =  num1>num2
    

    my_dict = {
        "var" : var,
        "msg" : greeting,
        "myfruits" : fruits,
        "num1":num1,
        "num2":num2,
        "ans":ans
    }
    return render(request,'third.html',context=my_dict)

def myimagepage(request):
    return render(request,'imagepage.html')

def myimagepage2(request):
    return render(request,'imagepage2.html')