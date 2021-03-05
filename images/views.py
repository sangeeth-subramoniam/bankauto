from django.shortcuts import render,redirect
from registration.models import user_profile
from .models import updimages
from .forms import updimages_form
# from .models import images

# Create your views here.

from django.views.generic.edit import UpdateView


class updimagesUpdateView(UpdateView):
    model = updimages
    fields = ['approval']
    template_name_suffix = '_update_form'




def unapproved(request,pk):

    curruser = request.user

    # if request.method == "POST":
        
    #     img_form = updimages_form(data = request.POST)
        
    #     if(img_form.is_valid() ):
            
    #         image = img_form.save(commit=False)
    #         image.owner = curruser
                    
    #         if 'img' in request.FILES:
    #             image.img = request.FILES['img']
            
    #         image.save()
        
    #     else:
    #         print(img_form.errors)


    # else:
    media_img = updimages.objects.filter(approval=False, user_profile__user__id = curruser.id)
    print(media_img,curruser)

    return render(request,"images/unapproved.html",{"curr_name" : curruser , "media" : media_img })



def approved(request,pk):

    curruser = request.user

    media_img = updimages.objects.all().filter(approval=True,user_profile__user__id = curruser.id)
    return render(request,"images/approved.html" , {"curr_name" : curruser , "media" : media_img })






def upload(request):

    if request.method == "POST":
        
        form = updimages_form(data=request.POST)

        if(form.is_valid()):
            
            images = form.save(commit=False)
            
                    
            if 'img' in request.FILES:
                images.img = request.FILES['img']
            
            images.save()
        
        else:
            print(form.errors)
    
    else:
        form = updimages_form()
        

    return render(request, "images/newupload.html", {'form': form } )

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if request.method == "POST":
    #     img2 = newupload(request.POST, request.FILES)
        
    #     if img2.is_valid():
    #         img2.save()

    #     else:
    #         print("error")
        
    #     return redirect("homepage:home")
    
    
    # else:
    #     updform = newupload()

    #     return render(request,"images/newupload.html",{"updform":updform})

        
        

