from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_profile(models.Model):

    #using default User model by linking 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #additional fields
    website = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures' )
    bio = models.CharField(blank=True, max_length=300)

    def __str__(self):
        return self.user.username