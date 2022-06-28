from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
import base64

from Admin.models import Advisor, Code
from Manifest.models import Manifest
from Student.models import Student
from Batch.models import Batch,Location,Branch
from Student.serializer import  LocationStudentSerializer
from .models import User, Profile, Domain, Notification
from .serializer import UserSerealizer, NotificationSerealizer, ProfileSerealizer, DomainSerealizer,getNotificationTypes,LocationSerealizer,BranchSerealizer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        if user.is_superuser:
            token['position'] = 'Admin'
        elif user.is_lead or user.is_staff or  user.is_student:
            token['position'] = user.department.name
            if user.is_student == True:
                token['photo'] = user.student.profile.photo
            elif user.is_staff == True:
                token['photo'] = user.advisor.profile.photo
        else:
            token['position'] = 'Outsider'
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerealizer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getNotifications(request):
    user = request.user
    if user.is_lead or user.is_staff:
        notification = NotificationSerealizer(Notification.objects.all().order_by('-id'), many=True).data
    else:
        notification = NotificationSerealizer(Notification.objects.exclude(type='BatchShift').exclude(type='Termination').order_by('-id'), many=True).data
    return Response(notification)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteNotifications(request):
    user = request.user
    if user.is_lead:
        Notification.objects.filter(id=request.data['id']).delete()
    return Response({'status': 'Success'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createNotifications(request):
    user = request.user
    if user.is_lead:
        Notification.objects.create(type = request.data['type'], content = request.data['content'], creator = user.username)
        return Response({"message": "Notification created successfully"})
    else:
        return Response({"message": "You are not authorized to create Notification"})
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getTypes(request):
    if request.user.is_lead:
       types = getNotificationTypes(Notification.objects.all(),many=True).data
       return Response(types)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    if user.is_staff:
            profile = Profile.objects.get(advisor=Advisor.objects.get(user=user))
    elif user.is_student:
        student = Student.objects.get(user=user)
        profile = Profile.objects.get(student=student)
        student.domain = Domain.objects.get(id=request.data['domain'])
        student.save()
    else:
        return Response({'error': 'You are not authorized to update profile'})
    profile.first_name = request.data['first_name']
    profile.last_name = request.data['last_name']
    profile.dob = request.data['dob']
    profile.gender = request.data['gender']
    profile.father = request.data['father']
    profile.father_contact = request.data['father_contact']
    profile.mother = request.data['mother']
    profile.mother_contact = request.data['mother_contact']
    profile.guardian = request.data['guardian']
    profile.relation = request.data['relation']
    profile.address = request.data['address']
    profile.village = request.data['village']
    profile.taluk = request.data['taluk']
    profile.education = request.data['education']
    profile.college = request.data['college']
    profile.experience = request.data['experience']
    profile.company = request.data['company']
    profile.designation = request.data['designation']
    profile.mobile = request.data['mobile']
    profile.govtid = request.data['govtid']
    profile.save()
    serealizer = ProfileSerealizer(profile)
    return Response(serealizer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getMyProfile(request):
    user = request.user
    if user.is_staff:
        profile = ProfileSerealizer(Profile.objects.get(advisor=Advisor.objects.get(user=user)))
    elif user.is_student:
        profile = ProfileSerealizer(Profile.objects.get(student=Student.objects.get(user=user)))
    else:
        student = Student.objects.filter(id=request.data['userId'])
        if len(student) == 0:
            advisor = Advisor.objects.filter(id=request.data['userId'])
            user = advisor[0].user
            profile = ProfileSerealizer(Profile.objects.get(advisor=advisor.get(id=request.data['userId'])))
        else:
            user = student[0].user
            profile = ProfileSerealizer(Profile.objects.get(student=student[0]))
    data = profile.data
    data['email'] = user.email
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getDomain(request):
    if request.user.is_lead or request.user.is_student :
        domain = DomainSerealizer(Domain.objects.all(), many=True).data
        return Response(domain)
    else:
        return Response({"message": "You are not authorized to view Domain"})

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

@api_view(['POST'])
def isLinkValid(request):
    link = request.data['link']
    print(link)
    if Batch.objects.filter(code=link).exists():
        batch = Batch.objects.get(code=link)
        branches = BranchSerealizer(Branch.objects.filter(location=batch.location), many=True).data
        return Response({"status":200, "message": "student", "batch": batch.id, "branches": branches})
    else:
        if Code.objects.filter(code=link).exists():
            locations = LocationSerealizer(Location.objects.all(), many=True).data
            return Response({"status":200, "message": "advisor", "branches": locations})
        else:
            return Response({"status":400, "message": "Code is not valid"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateProfilephoto(request):
    if request.user.is_staff:
        profile = Profile.objects.get(advisor=Advisor.objects.get(user=request.user))
    elif request.user.is_student:
        profile = Profile.objects.get(student=Student.objects.get(user=request.user))
    else:
        return Response({"message": "You are not authorized to update profile"})
    profile.photo = request.data['secure_url']
    profile.public_id = request.data['public_id']
    profile.signature = request.data['signature']
    profile.timestamp = request.data['timestamp']
    profile.save()
    return Response({"message": "Profile photo updated successfully"})

@api_view(['GET'])
def getLocations(request):
    locations = LocationSerealizer(Location.objects.all(), many=True).data
    return Response(locations)

        
@api_view(['POST'])
def getBranches(request):
    print(request.data)
    location = Location.objects.get(id=request.data['location'])
    branches = BranchSerealizer(Branch.objects.filter(location=location), many=True).data
    return Response(branches)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getBatchStudents(request):
    if request.user.is_staff:
        branch = Branch.objects.get(id=request.data['branch'])
        students = Student.objects.filter(branch=branch)
        for student in students:
            student.week = Manifest.objects.filter(student_name=student)[0]
            student.week = student.week.title[-2:]
            student.save()
        students = LocationStudentSerializer(students, many=True).data
        return Response(students)
    else:
        return Response({"message": "You are not authorized to view Location"})
