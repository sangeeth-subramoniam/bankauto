from django.shortcuts import render
from registration.models import user_profile

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        curruser = request.user
        return render(request,'landing/homepage.html',{'curr_user' : curruser})
    else:
        return render(request,'landing/homepage.html')

def contact(request):
    return render(request,'landing/contact.html')

def about(request):
    return render(request,'landing/about.html')