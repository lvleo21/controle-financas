from django.urls import path
from accounts.views import ClientCreateView

app_name = "accounts"
urlpatterns = [
    path("create_client", ClientCreateView.as_view(), name="create_client"),
]