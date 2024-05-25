from rest_framework import serializers
from .models import Prod_Serv_Nav

class Prod_Serv_NavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prod_Serv_Nav
        fields = '__all__'
        