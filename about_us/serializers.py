from rest_framework import serializers
from  .models import About_Us, Our_Certificate, Company_License

class About_UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Us
        fields = '__all__'

class Our_CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_Certificate
        fields = '__all__'

class Company_LicensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_License
        fields = '__all__'