from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from Admin.models import Advisor
from Batch.models import Batch
from User.models import Profile, Domain
from .models import Shifted, Student, Placement
from .serializer import ViewStudentSerializer, MyStudentSerializer, PlacementSerializer, TerminateRequestSerializer, ShiftRequestSerializer
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
        students = Student.objects.filter(batch__advisor=request.user.advisor, status__in=["Training", "RequestedTermination"])
        for student in students:
            student.week = Manifest.objects.filter(student_name=student).order_by('-id')[0].title
            student.pending = Tasks.objects.filter(week=Manifest.objects.filter(student_name=student)[0], status=False).count()
            student.save()
        serializer = MyStudentSerializer(students, many=True).data
        return Response(serializer)
    else:
        return Response({"error": "You are not authorized to view this page"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPlacements(request):
    if request.user.is_lead:
        students = Placement.objects.all()
        serializer = PlacementSerializer(students, many=True).data
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def shiftRequest(request):
    if request.user.is_staff:
        student = Student.objects.get(id=request.data['student'])
        Shifted.objects.create(student=student, shifted_to=Batch.objects.get(id=request.data['shift_to']), shifted_from=student.batch)
        return Response({"message": "Student Updated"})
    else:
        return Response({"message": "You are not authorized to perform this action"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def terminateRequest(request):
    if request.user.is_staff:
        Student.objects.filter(id=request.data['student']).update(status="RequestedTermination")
        return Response({"message": "Student Updated"})
    else:
        return Response({"message": "You are not authorized to perform this action"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getRequests(request):
    if request.user.is_lead:
        terminate = Student.objects.filter(status="RequestedTermination")
        shift = Shifted.objects.filter(status=False)
        for student in terminate:
            student.week = Manifest.objects.filter(student_name=student).order_by('-id')[0].title
            student.save()
        for student in shift:
            student.week = Manifest.objects.filter(student_name=student.student).order_by('-id')[0].title
            student.save()
        terminate = TerminateRequestSerializer(terminate, many=True).data
        shift = ShiftRequestSerializer(shift, many=True).data
        return Response({"terminate": terminate, "shift": shift})
    else:
        return Response({"message": "You are not authorized to perform this action"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def shiftAccept(request):
    if request.user.is_lead:
        shift = Shifted.objects.get(id=request.data['id'])
        Student.objects.filter(id=shift.student.id).update(batch=Batch.objects.get(id=shift.shifted_to.id))
        shift.status = True
        shift.save()
        return Response({"message": "Student Updated"})
    else:
        return Response({"message": "You are not authorized to perform this action"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def shiftReject(request):
    if request.user.is_lead:
        Shifted.objects.filter(id=request.data['id']).delete()
        return Response({"message": "Student Updated"})
    else:
        return Response({"message": "You are not authorized to perform this action"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def terminateAccept(request):
    if request.user.is_lead:
        Student.objects.filter(id=request.data['id']).update(status="Terminated")
        return Response({"message": "Student Updated"})
    else:
        return Response({"message": "You are not authorized to perform this action"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def terminateReject(request):
    if request.user.is_lead:
        Student.objects.filter(id=request.data['id']).update(status="Training")
        return Response({"message": "Student Updated"})
    else:
        return Response({"message": "You are not authorized to perform this action"})