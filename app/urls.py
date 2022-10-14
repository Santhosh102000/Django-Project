
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name="app1"


urlpatterns = [
    # path('',views.index,name="index"),
    path('',views.login,name="login"),
    path('welcome/',views.welcome,name='welcome'),
    path('homepage/',views.hometemp,name="homepage"),
    path('aboutus/',views.abouttemp,name="aboutus"),
    path('register/',views.register,name="register"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)