from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', views.halaman_utama, name='halaman_utama'),
    path('lingkaran/', views.tampilkan_halaman_lingkaran, name='halaman_lingkaran'),
    path('batang/', views.tampilkan_halaman_batang, name='halaman_batang'),
    path('garis/', views.tampilkan_halaman_garis, name='halaman_garis'),
    path('admin/', admin.site.urls),
    path('', include('aplikasiku.urls')),
]
