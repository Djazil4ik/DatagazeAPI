from rest_framework import generics
from .serializers import HomeSerializer, CertificateSerializer, PartnerSerializer, ContactSerializer, FieldOfActivitySerializer
from .models import Home, Certificate, Partner, Contact, FieldOfActivity

class HomeViewSet(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class CeritificateViewSet(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class PartnerViewSet(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class ContactViewSet(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class FieldOfActivityViewSet(generics.ListCreateAPIView):
    queryset = FieldOfActivity.objects.all()
    serializer_class = FieldOfActivitySerializer