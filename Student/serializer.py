
from rest_framework import serializers

from .models import Student, Placement, Shifted, EducationDetails
from User.serializer import UserSerealizer, ProfileSerealizer, DomainSerealizer
from Batch.serializer import BatchSerializer, GroupSerializer


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerealizer()
    batch = BatchSerializer()
    group = GroupSerializer()
    profile = ProfileSerealizer()
    domain = DomainSerealizer()
    class Meta:
        model = Student
        fields = '__all__'

class PlacementSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = Placement
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = EducationDetails
        fields = '__all__'

class ShiftedSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    shifted_to = BatchSerializer()
    shifted_in = BatchSerializer()
    class Meta:
        model = Shifted
        fields = '__all__'

        
class ViewStudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username')
    domain = serializers.CharField(source='domain.name',read_only=True)
    group = serializers.CharField(source='group.name',read_only=True, default='No Group')
    batch = serializers.CharField(source='batch.name',read_only=True)
    advisor = serializers.CharField(source='group.advisor.user.username',read_only=True, default='No Group')
    week = serializers.CharField()
    
    class Meta:
        model = Student
        fields = ('id','name','batch','group','advisor','week','domain')


class MyStudentSerializer(serializers.ModelSerializer):
    advisor = serializers.CharField(source='group.advisor.user.username', read_only=True, default='No Group')
    week = serializers.CharField()
    pending = serializers.IntegerField()
    name = serializers.CharField(source='user.username')
    batch = serializers.CharField(source='batch.name')
    class Meta:
        model = Student
        fields = ['id', 'name', 'batch', 'advisor', 'week', 'pending']


class TerminateRequestSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username')
    batch = serializers.CharField(source='batch.name')
    advisor = serializers.CharField(source='batch.advisor.user.username', read_only=True)
    week = serializers.CharField()
    class Meta:
        model = Student
        fields = ['id', 'name', 'batch', 'advisor', 'week']

class ShiftRequestSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='student.user.username')
    batch = serializers.CharField(source='shifted_from.name')
    advisor = serializers.CharField(source='shifted_from.advisor.user.username', read_only=True)
    week = serializers.CharField()
    class Meta:
        model = Shifted
        fields = ['id', 'name', 'batch', 'advisor', 'week']

class LocationStudentSerializer(serializers.ModelSerializer):
    user = UserSerealizer()
    batch = BatchSerializer()
    group = GroupSerializer()
    profile = ProfileSerealizer()
    week = serializers.CharField()
    class Meta:
        model = Student
        fields = '__all__'