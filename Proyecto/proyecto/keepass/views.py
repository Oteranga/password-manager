from http.client import UNAUTHORIZED
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from keepass.forms import RegisterForm
from keepass.keepass import check_password, delete_password,decript,check_fields_not_empty, decript, delete_password,save_register, authenticate_account, add_password, get_user_id, get_password,get_user_passwords, check_master_password
# Create your views here.

def login_page(request):
    if request.method == "GET":
      context = {}
      return render(request, 'login.html',context)
    if request.method == "POST":
      uname = request.POST['uname']
      psw = request.POST['psw']
      if check_fields_not_empty([uname,psw])==False:
        messages.success(request, "Empty fields")
      if authenticate_account(uname,psw):
        return HttpResponseRedirect('/main')
      else:
        messages.success(request, "INVALID ACCOUNT")
        return HttpResponseRedirect(request.path)



    return render(request,'login.html')

def register_page(request):
    if request.method == "GET":
      context = {}
      return render(request, 'register.html',context)
    if request.method == "POST":
      #Get the posted form
      uname = request.POST['uname']
      email = request.POST['email']
      psw = request.POST['psw']
      mpsw = request.POST['mpsw']
      if check_fields_not_empty([uname,email])==False:
        messages.success(request, "Empty fields")
      elif psw == mpsw:
        messages.success(request, "Your passwords are the same")
      elif check_password(psw) == False:
        messages.success(request, "Password is not secure")
      elif check_password(mpsw) ==False:
        messages.success(request, "MasterPassword is not secure")
      else:
        save_register(uname,email,psw,mpsw)
        return HttpResponseRedirect('/main')
      return HttpResponseRedirect(request.path)

      #verificar seguridad de contraseñas
      #si todo bien
        #hash contraseñas y guardar usuario retornar main_page
      #sino return register marcando errores
    else:
      MyLoginForm = RegisterForm()
    context = {}
    return render(request, 'register.html',context) 

def main_page(request):
    if request.method == "GET":
      context = {}
      id = get_user_id()
      psws = get_user_passwords(id)
      context['psws'] = psws
      return render(request,'index.html',context)
    if request.method == "POST":
      context = {}
      id = get_user_id()
      psws = get_user_passwords(id)
      context['psws'] = psws
      mpsw = request.POST['mpsw']
      mpsw_id = request.POST['mpsw_id']
      encripted_psw = get_password(mpsw_id).password
      print(mpsw)
      r, obj = check_master_password(mpsw)
      if r==True:
        print("SE LOGRO")
        context['password']=[decript(encripted_psw,obj)]
        context['password_id']=[mpsw_id]


        return render(request,'index.html',context)
      print("NO LOGRO")
      context = {}
      id = get_user_id()
      psws = get_user_passwords(id)
      context['psws'] = psws
      return render(request,'index.html',context)
      

def add_page(request):
    # render(request,'add_password.html')
    if request.method == "GET":
      context = {}
      return render(request, 'add_password.html',context)
    if request.method == "POST":
      #Get the posted form
      uname = request.POST['uname']
      email = request.POST['email']
      psw = request.POST['psw']
      site = request.POST['site']
      if check_fields_not_empty([uname,email,psw,site])==False:
        messages.success(request, "Empty fields")
      else:
        add_password(email,uname,psw,site)
        return HttpResponseRedirect('/main')
      return HttpResponseRedirect(request.path)

def edit_page(request):
    if request.method == "GET":
      v = request.GET['psw_id']
      print(v)
      delete_password(v)
      return HttpResponseRedirect('/main')

