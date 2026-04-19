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

def myimagepage3(request):
    return render(request,'imagepage3.html')
def myimagepage4(request):
    return render(request,'imagepage4.html')
def myimagepage5(request,imagename):
    myimagename = imagename
    imagename = myimagename.lower()
    print(myimagename)
    if myimagename == "django":
        var = True
    elif myimagename == "python":
        var = False
    mydictionary ={
        "var":var,
    }
    return render(request,'imagepage5.html',context=mydictionary)

def myform(request):
    return render(request,'myform.html')

def submitmyform(request):
    mydictionary = {
        "var1":request.POST['mytext'],
        "var2":request.POST['mymsg'],
        "method":request.method
    }
    return JsonResponse(mydictionary)