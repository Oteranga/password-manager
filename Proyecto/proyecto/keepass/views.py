from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from keepass.forms import RegisterForm
from keepass.keepass import check_password, check_fields_not_empty,save_register
# Create your views here.

def login_page(request):
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
    return render(request,'index.html')
