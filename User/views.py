from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from Admin.models import Advisor
from Student.models import Student
from .models import *
from .serializer import UserSerealizer, NotificationSerealizer, ProfileSerealizer, DomainSerealizer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['position'] = user.department.name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerealizer

# @api_view(['POST'])
# def get_user(request):
#     print("==============================")
#     print('request :::::::::::::', request)
#     print('User:::::::::::::', request.user)
#     print('User Name :::::::::::::', request.user.username)
#     print('Data :::::::::::::', request.data)
#     return Response({"name": request.user.username})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def notification(request):
    user = request.user
    if user.is_lead:
        notification = NotificationSerealizer(Notification.objects.all(), many=True)
        datas = {'dept': 'lead', 'notification': notification.data}
    elif user.is_staff:
        notification = NotificationSerealizer(Notification.objects.all(), many=True)
        datas = {'dept': 'advisor', 'notification': notification.data}
    else:
        notification = NotificationSerealizer(Notification.objects.exclude(type='BatchShift').exclude(type='Termination').order_by('date'), many=True)
        datas = {'dept': 'student', 'notification': notification.data}
    return Response(datas)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    if user.is_staff:
        profile = Profile.objects.get(advisor=Advisor.objects.get(user=user))
    elif user.is_student:
        profile = Profile.objects.get(student=Student.objects.get(user=user))
    else:
        return Response({'error': 'You are not authorized to update profile'})
    profile.first_name = request.data['first_name']
    profile.last_name = request.data['last_name']
    profile.domain = Domain.objects.get(id=request.data['domain'])
    profile.dob= request.data['dob']
    # profile.gender = request.data['gender'] 
    profile.address = request.data['address']
    profile.village = request.data['village']
    profile.education = request.data['education']
    profile.college = request.data['college']
    profile.experience = request.data['experience']
    profile.company = request.data['company']
    profile.designation = request.data['designation']
    profile.mobile = request.data['mobile']
    profile.save()
    profile = ProfileSerealizer(profile)
    return Response(profile.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    if user.is_staff:
        profile = ProfileSerealizer(Profile.objects.get(advisor=Advisor.objects.get(user=user)))
    elif user.is_student:
        profile = ProfileSerealizer(Profile.objects.get(student=Student.objects.get(user=user)))
    else:
        return Response({'error': 'You are not authorized to get profile'})
    data = profile.data
    print(data)
    data['email'] = user.email
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getDomain(request):
    if request.user.is_lead:
        domain = DomainSerealizer(Domain.objects.all(), many=True).data
        return Response(domain)
    else:
        return Response({"message": "You are not authorized to create Domain"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createDomain(request):
    if request.user.is_lead:
        Domain.objects.create( name=request.data['name'] )
        return Response({"message": "Domain created successfully"})
    else:
        return Response({"message": "You are not authorized to create Domain"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteDomain(request):
    if request.user.is_lead:
        Domain.objects.filter(id=request.data['id']).delete()
        return Response({"message": "Domain deleted successfully"})
    else:
        return Response({"message": "You are not authorized to delete Domain"})

@api_view(['POST'])
def updateDomain(request):
    if request.user.is_lead:
        Domain.objects.filter(id=request.data['id']).update(name=request.data['new_name'])
        return Response({"message": "Domain updated successfully"})
    else:
        return Response({"message": "You are not authorized to update Domain"})
