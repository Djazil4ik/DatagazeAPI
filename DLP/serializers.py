from rest_framework import serializers
from .models import *

class DatagazeDLPSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatagazeDLP
        fields = '__all__'


class PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parts
        fields = '__all__' 

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'

class I_and_CSerializer(serializers.ModelSerializer):
    class Meta:
        model = I_and_C
        fields = '__all__'

class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'