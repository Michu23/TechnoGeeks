from datetime import timedelta
from rest_framework import serializers
from .models import Department, User, Domain, Profile, Notification
from Admin.models import Advisor
from Student.models import Student
from Manifest.models import Manifest, Review
from Batch.models import Batch

class UserSerealizer(serializers.ModelSerializer):
    batch = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'is_staff', 'is_student', 'batch']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],email=validated_data['email']
            )
        user.set_password(validated_data['password'])

        if validated_data['is_staff']:
            user.department = Department.objects.get(name='Advisor')
            user.is_staff = True
            user.save()
            profile = Profile.objects.create()
            Advisor.objects.create(user=user, profile=profile)
        else:
            user.department = Department.objects.get(name='Student')
            user.is_student = True
            user.save()
            profile = Profile.objects.create()
            batch = Batch.objects.get(id = validated_data['batch'])
            student = Student.objects.create(user=user, profile=profile, batch=batch)
            day = student.batch.created_at + timedelta(days=7) if student.batch.created_at.strftime('%a') == "Sun" else student.batch.created_at + timedelta(days=8)
            Manifest.objects.create(title = 'Week 01',student_name=student, next_review=day)
        return user

class DomainSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('id', 'name')

class ProfileSerealizer(serializers.ModelSerializer):
    domain = DomainSerealizer()
    class Meta:
        model = Profile
        fields = '__all__'
        
class getNotificationTypes(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id','type')
        
class NotificationSerealizer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d/%m/%Y")
    class Meta:
        model = Notification
        fields = '__all__'