from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'registration'
urlpatterns = [
    path('signup', views.signup , name = "signup"),
    path('signin', views.signin , name = "signin"),
    path('signout', views.signout , name = "signout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
