from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Client(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(verbose_name="Idade")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name.upper()


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")
    is_active = models.BooleanField(verbose_name="Ativo?", default = False)

    def __str__(self):
        return self.name.upper()
    
class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50, verbose_name="Título") 
    value = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = "Valor")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")
    date_now = models.DateTimeField(auto_now_add=True)
    date_trasaction = models.DateField(verbose_name="Data da Transação")
    description = models.TextField(verbose_name="Descrição", blank=True)

    def __str__(self):
        return self.title.upper()



    




    

    
    
