from rest_framework import serializers

from .models import Student, Placement, Shifted
from User.serializer import UserSerealizer, ProfileSerealizer
from Batch.serializer import BatchSerializer, GroupSerializer


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerealizer()
    batch = BatchSerializer()
    group = GroupSerializer()
    profile = ProfileSerealizer()
    class Meta:
        model = Student
        fields = '__all__'

class PlacementSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = Placement
        fields = '__all__'

class ShiftedSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    shifted_to = BatchSerializer()
    shifted_in = BatchSerializer()
    class Meta:
        model = Shifted
        fields = '__all__'

class MyStudentSerializer(serializers.ModelSerializer):
    advisor = serializers.CharField(source='group.advisor.user.username', read_only=True)
    week = serializers.CharField()
    pending = serializers.IntegerField()
    name = serializers.CharField(source='user.username')
    class Meta:
        model = Student
        fields = ['id', 'name', 'advisor', 'week', 'pending']