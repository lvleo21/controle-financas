from django.urls import path
from accounts.views import ClientCreateView

app_name = "accounts"
urlpatterns = [
    path("create_client", ClientCreateView, name="create_client"),
]