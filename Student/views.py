from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from Batch.models import Batch
from User.models import Profile, Domain
from .models import Student
from Manifest.models import Manifest
from .serializer import ViewStudentSerializer, MyStudentSerializer
from Manifest.models import Manifest, Tasks


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getStudents(request):
    if request.user.is_lead or request.user.is_staff:
        students = Student.objects.all().order_by('batch')
        for student in students:
            student.week = Manifest.objects.filter(student_name=student).order_by('-id')[0].title
            student.save()
        serializer = ViewStudentSerializer(students, many=True).data
        return Response(serializer)
    else:
        return Response('You are not allowed to view this page')
        


# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getMyStudents(request):
    if request.user.is_staff:
        students = Student.objects.filter(batch__advisor=request.user.advisor)
        for student in students:
            student.week = Manifest.objects.filter(student_name=student).order_by('-id')[0].title
            student.pending = Tasks.objects.filter(week=Manifest.objects.filter(student_name=student)[0], status=False).count()
            student.save()
        serializer = MyStudentSerializer(students, many=True).data
        return Response(serializer)
    else:
        return Response({"error": "You are not authorized to view this page"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def manageStudent(request):
    if request.user.is_lead:
        student = Student.objects.get(id=request.data['student'])
        student.batch = Batch.objects.get(id=request.data['batch'])
        student.save()
        Profile.objects.filter(student=student).update(domain=Domain.objects.get(id=request.data['domain']))
        return Response({"message": "Student Updated"})
    else:
        return Response({"message": "You are not authorized to perform this action"})

