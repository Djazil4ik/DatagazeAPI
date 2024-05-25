from django.urls import path, include
from .views import HomeViewSet, CeritificateViewSet, PartnerViewSet, ContactViewSet, FieldOfActivityViewSet
from rest_framework import routers

urlpatterns = [
    path('home/', HomeViewSet.as_view()),
    path('certificate/', CeritificateViewSet.as_view()),
    path('partner/', PartnerViewSet.as_view()),
    path('contact/', ContactViewSet.as_view()),
    path('fieldsofactivity/', FieldOfActivityViewSet.as_view()),
]