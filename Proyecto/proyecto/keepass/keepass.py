
from .models import User
import re
from hashlib import pbkdf2_hmac 
import secrets 

def check_fields_not_empty(fields):
    for i in fields:
        if i and i.strip():
            continue
        else:
            return False
    return True
        

def check_password(psw):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{12,100}$"
    pat = re.compile(reg) 
    mat = re.search(pat, psw) 
    if mat: 
        return True
    else: 
        return False

def hash_password(psw,salt):
    our_app_iters = 500_000  # Application specific, read above.
    #ver que usaremos de 
    dk = pbkdf2_hmac('sha512', bytes(psw,'utf-8'), salt, our_app_iters)
    return dk.hex()

def save_register(uname,e_mail,psw,mpsw):
    u_salt = secrets.token_bytes(64)
    new_user = User(
        username= uname,
        email= e_mail,
        user_password = hash_password(psw,u_salt),
        masterpassword = hash_password(mpsw,u_salt),
        salt=u_salt.hex()
    )
    new_user.save()

def authenticate_account(uname,psw):
    obj = User.objects.filter(username=uname)
    if not obj:
        return False
    account = obj[0 ]
    salt = bytes.fromhex(account.salt)
    if account.user_password == hash_password(psw,salt):
        return True
    else:
        return False
#-> Fabo#71563516