from django.shortcuts import render
from .forms import User_form , user_profile_form

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def signup(request):
    registered = False

    if request.method == "POST":
        
        user_form = User_form(data=request.POST)
        user_profileform = user_profile_form(data=request.POST)

        if(user_form.is_valid() and user_profileform.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profileform.save(commit=False)
            profile.user = user
            

                    
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            
            profile.save()

            registered = True
        
        else:
            print(user_form.errors, user_profileform.errors)
    
    else:
        user_form = User_form()
        user_profileform = user_profile_form()

    return render(request, "authenticate/signup.html", {'user_form': user_form , 'user_profileform' : user_profileform, 'registered' : registered  } )


# Create your views here.

def signin(request):
    context = {}
    
    if(request.method == "POST"):
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('homepage:home'))
            
            else:
                return HttpResponse('account is NOT Active')
            
        else:
            print("someone tried to login and failed")
            print("username: {} and password {}".format(username,password))
            return HttpResponse("invalid login supplied")
    
    else:
        return render(request,'authenticate/signin.html' , context)


@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage:home"))
