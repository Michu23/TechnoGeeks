from rest_framework import serializers
from Student.models import Student

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
        fields = ('id', 'name', 'advisor', 'student', 'placement', 'code')

class ViewGroupSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.count')
    advisor = serializers.CharField(source='advisor.user.username', read_only=True)
    domain = serializers.CharField(source='domain.name', read_only=True)
    batch = serializers.CharField(source='batch.name', read_only=True)
    class Meta:
        model = Group
        fields = '__all__'

class StudentGroupSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    week = serializers.CharField()
    class Meta:
        model = Student
        fields = ('id', 'user', 'week')

class ViewGroupDetailsSerializer(serializers.ModelSerializer):
    student = StudentGroupSerializer(many=True)
    domain = serializers.CharField(source='domain.name', read_only=True)
    batch = serializers.CharField(source='batch.name', read_only=True)
    class Meta:
        model = Group
        fields = ('id', 'domain', 'batch', 'student')

class GroupStudentDetailsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username', read_only=True)
    week = serializers.CharField()
    pending = serializers.IntegerField()
    count = serializers.IntegerField()
    class Meta:
        model = Student
        fields = ('id', 'name', 'week', 'pending', 'count')