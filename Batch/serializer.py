from rest_framework import serializers
from .models import Batch, Group
from User.serializer import DomainSerealizer
from Admin.serializer import AdvisorSerializer

class BatchSerializer(serializers.ModelSerializer):
    advisor = AdvisorSerializer()
    class Meta:
        model = Batch
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    batch = BatchSerializer()
    domain = DomainSerealizer()
    advisor = AdvisorSerializer()
    class Meta:
        model = Group
        fields = '__all__'