from django.forms import ModelForm
from .models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserForm(ModelForm):
    class Meta:
        model=User
        fields="__all__"
    
   