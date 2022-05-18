from rest_framework import serializers
from .models import Advisor
from User.serializer import UserSerealizer, ProfileSerealizer

class AdvisorSerializer(serializers.ModelSerializer):
    user = UserSerealizer()
    profile = ProfileSerealizer()
    class Meta:
        model = Advisor
        fields = '__all__'