
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('login', views.user_login, name='user_login'),  # Burada 'name' parametresini ekledim
    path('kayıt', views.user_register,name='user_register'),
]

#'tek tıranak olan kısımlar web sayfasındaki url tarafındaki kod sayısı ya da metni
#(view.) ise views.py deki fonksiyonları çalıştırmayı yarıyor
