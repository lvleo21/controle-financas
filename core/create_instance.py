
from core.models import *
from datetime import date

CREATE_INSTANCES_TRANSACTION = False

def create_transaction(user):
     if CREATE_INSTANCES_TRANSACTION:
         client = Client.objects.get(user = user)
         title = "borracha"
         value = "1.00"
         category = Category.objects.get(name="escolar")


         transaction = Transaction(
             client = client,
             title = title,
             value = value,
             category = category,
             date_trasaction = date.today(),

         )

         transaction.save()

