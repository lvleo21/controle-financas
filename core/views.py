from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.models import *
from core.forms import *

from django.http import HttpResponseRedirect
from django.http.response import JsonResponse


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

    def get_category_by_user(self, user):
        category = Category.objects.all()

        if (user.is_superuser is False):
            category = Category.objects.filter(client__user = user, is_active = True)
        
        return category

    def get_context_data(self, **kwargs):
        context = super(TransactionUpdateView, self).get_context_data(**kwargs)
        context['form'].fields['category'].queryset = self.get_category_by_user(self.request.user)
        return context

class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy('core:list_transaction')

#! Category
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "core/modules/category/list_category.html"
    context_object_name = "categories"
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        qs  = super(CategoryListView, self).get_queryset(*args, **kwargs)
        if self.request.user.is_superuser is False:
            qs = qs.filter(client__user = self.request.user)
        return qs

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    
    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER")




class CategoryCreateView(LoginRequiredMixin, View):
    model = Category
    form_class = CategoryForm

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            temp_client = Client.objects.get(user = self.request.user)
            self.object.client = temp_client
            self.object.save()
            
            data = {
                "status": 200,
                "id": self.object.pk,
                "name": self.object.name.upper(),
            }

        else:

            data = {
                "status": 500,
                "id": None,
                "name": None,
            }
        return data
        

        
        

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        data = self.form_valid(form)
        return JsonResponse(data)


def create_category_modal(request):
    data = {}
    name = request.GET.get("name", None)

    if name is None:
        data['is_none'] = True 
    else:
        try:
            temp_category = Category.objects.get(name = name)
            data['is_exist'] = True

        except Category.DoesNotExist:
            temp_client = Client.objects.get(user = request.user)
            new_category = Category(name=name, client=temp_client)
            new_category.save()


            print("PK",new_category.pk)
            data['success'] = True
            data['obj'] = {
                'name': new_category.name.upper(),
                'id': new_category.pk
            }


    return JsonResponse(data)




    
#! Page 404
def page_404_view(request, exception):    
    template_name = "core/pages/404.html"

    path = request.path
    
    if path.startswith("/update/"):
        error = "update"
    else:
        error = None
    
    
    data = {
        'error': error
    }
    
    return render(request, template_name, data)

 
