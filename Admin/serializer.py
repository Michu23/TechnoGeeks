from rest_framework import serializers
from .models import Advisor
from User.serializer import UserSerealizer, ProfileSerealizer
from Batch.serializer import BatchSerializer

class AdvisorSerializer(serializers.ModelSerializer):
    user = UserSerealizer()
    profile = ProfileSerealizer()
    class Meta:
        model = Advisor
        fields = '__all__'

class AdvisorHalfSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    class Meta:
        model = Advisor
        fields = ('id', 'username')

class AdvisorFullSerealizer(serializers.ModelSerializer):
    batches = BatchSerializer(many=True)
    user = serializers.CharField(source='user.username')
    group = serializers.CharField(source='group.count')
    class Meta:
        model = Advisor
        fields = ('id', 'user', 'batches', 'groups')