from django.shortcuts import render

from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(Request):
    return HttpResponse('<h1>Welcome to the Login Page</h1>')

# def hainame(request,name):
#     return HttpResponse('<h2> Hello{} </h2>'.format(name))

# def home(request):
#     return HttpResponse("<h1> Welcome to homepage</h1>")

# def add(request,a,b):
#     return HttpResponse("<h1>Sum of{} and {} is {}</h1>".format(a,b,int(a)+int(b)))

# def templatedemo(request):
#     fruits={'apple','mango','papaya','banana'}
#     return render(request,"template1.html",
#     context={'name':"sandy",'profession':"software Engineer",'fruits':fruits})

def login(request):
    return render(request,'login.html')

def welcome(request):
    return render(request,'welcome.html')

def hometemp(request):
    return render(request,'Pages/home.html')

def abouttemp(request):
    return render(request,'Pages/about.html')

def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        if request.FILES:
            file=request.FILES['profilepic']
            fs=FileSystemStorage()
            saved_file=fs.save(file.name,file)
            file_url=fs.url(saved_file)
        return HttpResponse("<h1>Sucess</h1>")
    return render(request,"Pages/register.html")






