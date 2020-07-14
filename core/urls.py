
from django.urls import path
from core.views import *

app_name = "core"
urlpatterns = [
    path("", TrasactionListView.as_view(), name="list_transaction"),
    path("create/", TransactionCreateView.as_view(), name="create_transaction"),
    path("update/<int:pk>/", TransactionUpdateView.as_view(), name="update_transaction"),
    path("delete/<int:pk>/", TransactionDeleteView.as_view(), name="delete_transaction"),
    path("create-category/", CategoryCreateView.as_view() , name="create_category"),
    path("list-category/", CategoryListView.as_view() , name="list_category"),
    path("delete-category/<int:pk>/", CategoryDeleteView.as_view() , name="delete_category"),

]   
