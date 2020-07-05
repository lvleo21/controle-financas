from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.models import *
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from core.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from core.create_instance import create_transaction

class TrasactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "core/list_transaction.html"
    context_object_name = "transactions"
    paginate_by = 9

    

    def get_queryset(self, *args, **kwargs):
        qs = super(TrasactionListView, self).get_queryset(*args, **kwargs) 
        search = self.request.GET.get("id_search", None)
        qs = qs.filter(client__user = self.request.user)
        create_transaction(self.request.user)
        if search is not None:
            qs = qs.filter(title__icontains = search)
        

        
        return qs 

      
class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "core/create_transaction.html"
    success_url = reverse_lazy('core:list_transaction')

    def get_category_by_user(self, user):
        category = Category.objects.all()

        if (user.is_superuser is False):
            category = Category.objects.filter(client__user = user)
        
        return category

    def get_context_data(self, **kwargs):
        context = super(TransactionCreateView, self).get_context_data(**kwargs)
        context['form'].fields['category'].queryset = self.get_category_by_user(self.request.user)
        return context

    def form_valid(self, form):
        self.object = form.save()
        temp_client = Client.objects.get(user = self.request.user)
        self.object.client = temp_client
        self.object.save()

        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "core/update_transaction.html"
    success_url = reverse_lazy('core:list_transaction')


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy('core:list_transaction')
    




    

    
    


 
