from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'images'

urlpatterns = [
    path('unapproved/<str:pk>', views.unapproved , name = "unapproved") ,
    path('approved/<str:pk>', views.approved , name = "approved") , 
    path('update/<int:pk>', views.updimagesUpdateView.as_view() , name = "update"),
    path('newupload', views.upload , name = "upload") , ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
