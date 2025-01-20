from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

# Create your models here.

class User(AbstractUser):
    has_profile = models.BooleanField(default=False)



class UserProfile(models.Model):
    bio = models.TextField(null=True, blank=True)
    profile_pics = models.ImageField(upload_to='profile_pics/',validators=[FileExtensionValidator(['png'])],null=True,blank=True)