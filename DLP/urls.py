from django.urls import path
from .views import *

urlpatterns = [
    path('dlp/', DatagazeDLPViewSet.as_view(), name='dlp'),
    path('parts/', PartsViewSet.as_view(), name='parts'),
    path('features/', FeaturesViewSet.as_view(), name='features'),
    path('channels/', ChannelViewSet.as_view(), name='channels'),
    path('env/', EnvironmentViewSet.as_view(), name='env'),
    path('i-c/', I_and_CViewSet.as_view(), name='i-c'),
    path('screenshot/', ScreenshotViewSet.as_view(), name='screenshot'),
    path('video/', VideoViewSet.as_view(), name='video'),
    path('order/', OrderViewSet.as_view(), name='order'),
]