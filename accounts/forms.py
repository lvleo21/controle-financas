from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.models import Client

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1","password2"]


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
 
