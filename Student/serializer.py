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

        
class ViewStudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username')
    domain = serializers.CharField(source='profile.domain.name',read_only=True)
    group = serializers.CharField(source='group.name',read_only=True)
    batch = serializers.CharField(source='batch.batchno',read_only=True)
    advisor = serializers.CharField(source='batch.advisor.user.username',read_only=True)
    week = serializers.CharField()
    
    class Meta:
        model = Student
        fields = ('id','name','batch','group','advisor','week','domain')


class MyStudentSerializer(serializers.ModelSerializer):
    advisor = serializers.CharField(source='group.advisor.user.username', read_only=True)
    week = serializers.CharField()
    pending = serializers.IntegerField()
    name = serializers.CharField(source='user.username')
    class Meta:
        model = Student
        fields = ['id', 'name', 'advisor', 'week', 'pending']
>>>>>>> ab975782a8570328ec7ec1125a054bbd143c289a
