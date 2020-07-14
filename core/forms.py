from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.models import *





class TransactionForm(ModelForm):

    class Meta:
        model = Transaction
        fields = "__all__"
        exclude = ["client", ]

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        exclude = ["client", "is_active", ]



   