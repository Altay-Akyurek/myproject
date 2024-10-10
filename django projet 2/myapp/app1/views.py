from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

def user_login(request):
    if request.method== "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login (request,user)
            return render(request,"index.html")
        else:
            return render(request,"login.html",{"error":"username ya da parola yanlış"})
    else:
        return render(request,"login.html")
def user_register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]
#burada hata var düzelt
#buradaki hata re-password taradındaki name ve id kısımları hata yapıyordu düzeltildi
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"register.html",{"error":"username kullanılırıyor"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"register.html",{"error":"email kullanılıyor"})
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    return render(request,"index.html")
        else:
            return render(request,"register.html",{"error":"parolo eşleşmiyor"})
    else:
        return render(request ,"register.html")
def user_logout(request):
    return render(request,"index.html")



def home(request):
    return render(request, "login.html")

