from rest_framework import serializers
from .models import Payment
from Student.models import Student

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'