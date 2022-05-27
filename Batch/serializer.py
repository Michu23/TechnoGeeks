from rest_framework import serializers
from Student.models import Student
from Manifest.models import Manifest
from User.serializer import ProfileSerealizer, UserSerealizer
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
    domain = serializers.CharField(source='domain.name', read_only=True)
    batch = serializers.CharField(source='batch.batchno', read_only=True)
    class Meta:
        model = Group
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    week = serializers.CharField()
    class Meta:
        model = Student
        fields = ('id', 'user', 'week')

class ViewGroupDetailsSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)
    domain = serializers.CharField(source='domain.name', read_only=True)
    batch = serializers.CharField(source='batch.batchno', read_only=True)
    class Meta:
        model = Group
        fields = ('id', 'domain', 'batch', 'student')

class ViewMyGroupsSerializer(serializers.ModelSerializer):
    student = serializers.IntegerField()
    domain = serializers.CharField(source='domain.name', read_only=True)
    batch = serializers.CharField(source='batch.batchno', read_only=True)
    class Meta:
        model = Group
        fields = ('id', 'name', 'domain', 'batch', 'student')