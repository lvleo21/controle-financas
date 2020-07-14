from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.models import *
from betterforms.multiform import MultiModelForm
from six import python_2_unicode_compatible

class TransactionForm(ModelForm):

    class Meta:
        model = Transaction
        fields = "__all__"
        exclude = ["client",]

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", ]

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        exclude = ["user",]


class UserClientForm(MultiModelForm):
    form_classes = {
        'user': UserForm,
        'client': ClientForm,
    }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        exclude = ["client", "is_active", ]

        