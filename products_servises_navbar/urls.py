from django.urls import path
from .views import Prod_Serv_NavViewSet

urlpatterns = [
    path('', Prod_Serv_NavViewSet.as_view())
]