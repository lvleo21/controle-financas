from django.shortcuts import render
from django.views.generic import *
from core.models import Client
from core.forms import UserClientForm
from django.urls import reverse_lazy

class ClientCreateView(CreateView):
    model = Client
    form_class = UserClientForm
    template_name = "client/create_client.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form['user'].save()

        client = form['client'].save(commit=False)
        client.user = user
        client.save()
        return super().form_valid(form)