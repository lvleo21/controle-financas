from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.models import *
from core.forms import *



#! Transaction
class TrasactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "core/modules/transaction/list_transaction.html"
    context_object_name = "transactions"
    paginate_by = 8

    
    def get_context_data(self, **kwargs):
        context = super(TrasactionListView, self).get_context_data(**kwargs)
        context['search_not_exist'] = True if (context['transactions'].count() == 0 and self.request.GET) else False
        context.update()
        return context
    
    def get_queryset(self, *args, **kwargs):
        qs = super(TrasactionListView, self).get_queryset(*args, **kwargs) 
        search = self.request.GET.get("id_search", None)
        
        

        if self.request.user.is_superuser is False:
            qs = qs.filter(client__user = self.request.user)
        
        if search is not None:
            qs = qs.filter(title__icontains = search)

        return qs 

  

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "core/modules/transaction/create_transaction.html"
    success_url = reverse_lazy('core:list_transaction')

    def get_category_by_user(self, user):
        category = Category.objects.all()

        if (user.is_superuser is False):
            category = Category.objects.filter(client__user = user, is_active = True)
        
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
    template_name = "core/modules/transaction/update_transaction.html"
    success_url = reverse_lazy('core:list_transaction')

class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy('core:list_transaction')

#! Category
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "core/modules/category/list_category.html"
    context_object_name = "categories"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs  = super(CategoryListView, self).get_queryset(*args, **kwargs)
        if self.request.user.is_superuser is False:
            qs = qs.filter(client__user = self.request.user)
        return qs

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("core:list_category")


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "core/modules/category/create_category.html"
    success_url = reverse_lazy('core:list_category')

    def form_valid(self, form):
        self.object = form.save()
        temp_client = Client.objects.get(user = self.request.user)
        self.object.client = temp_client
        self.object.save()
        return super().form_valid(form)





    
    


 
