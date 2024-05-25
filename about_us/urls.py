from django.urls import path
from .views import About_UsViewSet, Our_CertificateViewSet, Company_LicenseViewSet

urlpatterns = [
    path('about/', About_UsViewSet.as_view()),
    path('our_certificates/', Our_CertificateViewSet.as_view()),
    path('company_licenses/', Company_LicenseViewSet.as_view()),
]