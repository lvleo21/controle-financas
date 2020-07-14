from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import *
from core.models import Client
from accounts.forms import UserForm, ClientForm


def ClientCreateView(request):
    template_name = "client/create_client.html"

    user_form = UserForm(request.POST or None)
    client_form = ClientForm(request.POST or None)

    context = {
        'user': user_form,
        'client': client_form,
    }

    if user_form.is_valid() and client_form.is_valid():
        user = user_form.save()
        client = client_form.save(commit=False)
        client.user = user
        client.save()

        return redirect("login")

    return render(request, template_name, context)