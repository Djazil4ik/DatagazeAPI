from rest_framework import generics
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer