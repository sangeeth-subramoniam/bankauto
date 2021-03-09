from django.shortcuts import render,redirect
from registration.models import user_profile
from .models import updimages,updimagestext
from .forms import updimages_form


import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\s-sangeeth-k\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image


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

    media_img = updimages.objects.filter(approval=True,user_profile__user__id = curruser.id)
    print('hola hola hola 111111111111111111117' , media_img)
    # a = media_img.updimagestext_set.all()
    
    
    
    
    

    
    # content = updimagestext.objects.all().filter(updimage__id = updimage__img__id)
    # print(content)


    return render(request,"images/approved.html" , {"curr_name" : curruser , "media" : media_img })






def upload(request):

    if request.method == "POST":
        
        form = updimages_form(data=request.POST)

        if(form.is_valid()):
            
            images = form.save(commit=False)
            
                    
            if 'img' in request.FILES:
                images.img = request.FILES['img']
                
            
            images.save()
            filename = request.FILES['img'].name
            # filename = request.FILES.get(images.img.name, 'noneisthere')
            fp = "media/upd/" + filename
            txt = tess.image_to_string(fp)
            cont = updimagestext.objects.create(text = txt)
            # images.content = txt
            to_update = updimages.objects.filter(id=images.id).update(content=txt)
            print('idhu content la sethachi ' , images.content)
        
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

        
        

