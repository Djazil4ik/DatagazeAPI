from rest_framework import generics
from .models import Prod_Serv_Nav
from .serializers import Prod_Serv_NavSerializer

class Prod_Serv_NavViewSet(generics.ListCreateAPIView):
    queryset = Prod_Serv_Nav.objects.all()
    serializer_class = Prod_Serv_NavSerializer