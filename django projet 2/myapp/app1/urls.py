
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('anasayfa',views.home),
    path('kurslar',views.kurslar),
]
#'tek tıranak olan kısımlar web sayfasındaki url tarafındaki kod sayısı ya da metni
#(view.) ise views.py deki fonksiyonları çalıştırmayı yarıyor
