
from .models import Password, User
import re
from hashlib import pbkdf2_hmac 
import secrets 


user_id = 15


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
    account = obj[0]
    salt = bytes.fromhex(account.salt)
    if account.user_password == hash_password(psw,salt):
        global user_id
        user_id= account.id
        return True
    else:
        return False

def add_password(e_mail,uname,psw,site):
    global user_id
    print(user_id)

    new_psw = Password(
        user = User.objects.filter(id=user_id)[0],
        username= uname,
        email= e_mail,
        password = psw,
        destination_url = site
    )
    new_psw.save()

def get_user_passwords(id):
    user_passwords = Password.objects.filter(user_id=id)
    return user_passwords

def get_password(id):
    user_passwords = Password.objects.filter(id=id)
    return user_passwords[0]
#-> Fabrizio$301200

def get_user_id():
    global user_id
    return user_id 
    
def check_master_password(mpsw):
    global user_id
    obj = User.objects.filter(id=user_id)
    account = obj[0]
    salt = bytes.fromhex(account.salt)
    if account.masterpassword == hash_password(mpsw,salt):
        return True, account.masterpassword
    else:
        return False, ""