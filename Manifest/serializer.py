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

class ReviewListSerealizer(serializers.ModelSerializer):
    created = serializers.DateField(format="%d/%m/%Y")
    reviewer = serializers.CharField(source='reviewer.name')
    class Meta:
        model = Review
        fields = ('id', 'created', 'reviewer', 'remark')

class StudentTasklistSerializer(serializers.ModelSerializer):
    week = serializers.CharField(source='title', read_only=True)
    tech_mark = serializers.IntegerField(source='technical_score', read_only=True)
    misc_mark = serializers.IntegerField(source='misc_score', read_only=True)
    pending = serializers.IntegerField()
    reviews = ReviewListSerealizer(many=True)
    next_review = serializers.DateField(format="%d/%m/%Y")
    class Meta:
        model = Manifest
        fields = ['id', 'week', 'pending', 'tech_mark', 'misc_mark', 'reviews', 'next_review']

class TaskSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'taskname', 'status', 'created']

class ManifestTaskSerealizer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student_name.user.username', read_only=True)
    tasks = TaskSerealizer(many=True)
    class Meta:
        model = Manifest
        fields = ['id', 'title', 'student_name', 'personal_wo', 'technical_score', 'misc_score', 'is_complete', 'tasks', 'folder']