from django.shortcuts import render

# Create your views here.

def login_page(request):
    return render(request,'login.html')

def register_page(request):
    return render(request,'register.html')

def main_page(request):
    return render(request,'index.html')
