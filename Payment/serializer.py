from rest_framework import serializers
from .models import Payment
from Student.models import Student

class PaymentSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.username')
    batch = serializers.CharField(source='student.batch.name')
    class Meta:
        model = Payment
        fields = ['id', 'student', 'batch','month','amount', 'totalamt', 'paid_date','types','status','paid','paymentid']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
        depth = 2