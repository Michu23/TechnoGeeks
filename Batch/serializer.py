from tkinter import Place
from rest_framework import serializers

from Student.models import Placement, Student
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

class ViewBatchSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.count')
    placement = serializers.CharField(source='placement.count')
    advisor = serializers.CharField(source='advisor.user.username', read_only=True)
    class Meta:
        model = Batch
        fields = ('id', 'batchno', 'advisor', 'location', 'student', 'placement')

class ViewGroupSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.count')
    advisor = serializers.CharField(source='advisor.user.username', read_only=True)
    domain = serializers.CharField(source='domain.name')
    class Meta:
        model = Group
        fields = '__all__'