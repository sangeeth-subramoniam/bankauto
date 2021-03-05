from django.db import models
from django.contrib.auth.models import User
from registration.models import user_profile

from django.urls import reverse


# Create your models here.

class updimages(models.Model):

    user_profile = models.ForeignKey("registration.user_profile", on_delete=models.CASCADE)
    img = models.ImageField(upload_to='upd' , blank = True)
    content = models.CharField(max_length=200, blank=True)
    approval = models.BooleanField(default=False)

    def __str__(self):
        name = self.user_profile.user.username
        return ("image"+str(name))

    def get_absolute_url(self):
        return reverse('homepage:home')
    

