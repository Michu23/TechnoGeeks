from rest_framework import serializers
from .models import Manifest, Review, Tasks, DataStructure, DS_Review
from User.serializer import UserSerealizer
from Student.serializer import StudentSerializer

class ManifestSerealizer(serializers.ModelSerializer):
    student_name = StudentSerializer()
    class Meta:
        model = Manifest
        fields = '__all__'

class ReviewSerealizer(serializers.ModelSerializer):
    manifest = ManifestSerealizer()
    class Meta:
        model = Review
        fields = '__all__'

class TasksSerealizer(serializers.ModelSerializer):
    week = ManifestSerealizer()
    class Meta:
        model = Tasks
        fields = '__all__'

class DataStructureSerealizer(serializers.ModelSerializer):
    user = UserSerealizer()
    class Meta:
        model = DataStructure
        fields = '__all__'

class DS_ReviewSerealizer(serializers.ModelSerializer):
    ds = DataStructureSerealizer()
    class Meta:
        model = DS_Review
        fields = '__all__'