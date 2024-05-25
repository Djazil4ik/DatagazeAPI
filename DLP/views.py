from rest_framework import generics
from .models import *
from .serializers import *

class DatagazeDLPViewSet(generics.ListCreateAPIView):
    queryset = DatagazeDLP.objects.all()
    serializer_class = DatagazeDLPSerializer

class PartsViewSet(generics.ListCreateAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartsSerializer

class FeaturesViewSet(generics.ListCreateAPIView):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer

class ChannelViewSet(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class EnvironmentViewSet(generics.ListCreateAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer

class I_and_CViewSet(generics.ListCreateAPIView):
    queryset = I_and_C.objects.all()
    serializer_class = I_and_CSerializer

class ScreenshotViewSet(generics.ListCreateAPIView):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer

class VideoViewSet(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class OrderViewSet(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer