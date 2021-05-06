from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'homepage'

urlpatterns = [
    path('', views.home , name = "home"),
    path('contact', views.contact , name = "contact"),
    path('about', views.about , name = "about"),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
