from rest_framework import generics
from .models import About_Us, Our_Certificate, Company_License
from .serializers import About_UsSerializer, Our_CertificatesSerializer, Company_LicensesSerializer

class About_UsViewSet(generics.ListCreateAPIView):
    queryset = About_Us.objects.all()
    serializer_class = About_UsSerializer

class Our_CertificateViewSet(generics.ListCreateAPIView):
    queryset = Our_Certificate.objects.all()
    serializer_class = Our_CertificatesSerializer

class Company_LicenseViewSet(generics.ListCreateAPIView):
    queryset = Company_License.objects.all()
    serializer_class = Company_LicensesSerializer
