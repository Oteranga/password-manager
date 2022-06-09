import email
from django.shortcuts import render
from keepass.forms import RegisterForm
# Create your views here.

def login_page(request):
    return render(request,'login.html')

def register_page(request):
    if request.method == "POST":
      #Get the posted form
      uname = request.POST['uname']
      email = request.POST['email']
      psw = request.POST['psw']
      mpsw = request.POST['mpsw']
      #verificar seguridad de contraseñas
      #si todo bien
        #hash contraseñas y guardar usuario retornar main_page
      #sino return register marcando errores
    else:
        MyLoginForm = RegisterForm()
    return render(request,'register.html')
		
    return render(request, 'loggedin.html', {"username" : username})
    return render(request,'register.html')

def main_page(request):
    return render(request,'index.html')
