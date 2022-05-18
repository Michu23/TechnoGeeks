from rest_framework import serializers
from .models import User, Domain, Profile
from Admin.models import Advisor
from Student.models import Student

class UserSerealizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'is_superuser', 'is_lead', 'is_staff', 'is_student')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],email=validated_data['email']
            )
        user.set_password(validated_data['password'])

        if validated_data['is_superuser']:
            user.is_superuser = True
            user.save()
        if validated_data['is_lead']:
            user.is_lead = True
            user.save()
        if validated_data['is_staff']:
            user.is_staff = True
            user.save()
            profile = Profile.objects.create()
            Advisor.objects.create(user=user, profile=profile)
        else:
            user.is_student = True
            user.save()
            profile = Profile.objects.create()
            Student.objects.create(user=user, profile=profile)
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
