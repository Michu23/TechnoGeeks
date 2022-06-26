from re import A
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Student.models import Placement, Student
from Manifest.models import Manifest
from Manifest.models import Review
from Manifest.models import Tasks
from .models import Batch, Group
from Admin.models import Advisor
from User.models import Domain
from .serializer import StudentGroupSerializer, ViewBatchSerializer, ViewGroupSerializer, ViewGroupDetailsSerializer, GroupStudentDetailsSerializer
from .utils import generateLink
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getBatches(request):
    if request.user.is_lead or request.user.is_staff:
        batchs = Batch.objects.all()
        batchsArray = []
        for batch in batchs:
            batch.placement = Placement.objects.filter(student__batch=batch)
            batch.student = Student.objects.filter(batch=batch)
            batch.save()
            serializer = ViewBatchSerializer(batch).data
            batchsArray.append(serializer)
        return Response(batchsArray)
    else:
        return Response({"message": "You are not authorized to view Batch"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createBatch(request):
    if request.user.is_lead:
        advisor = Advisor.objects.get(id=request.data['advisor'])
        Batch.objects.create( name=request.data['name'], advisor=advisor, code=generateLink(request.data['name']))
        return Response({"message": "Batch created successfully"})
    else:
        return Response({"message": "You are not authorized to create Batch"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteBatch(request):
    if request.user.is_lead:
        Batch.objects.filter(id=request.data['id']).delete()
        return Response({"message": "Batch deleted successfully"})
    else:
        return Response({"message": "You are not authorized to delete Batch"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateBatch(request):
    if request.user.is_lead:
        Batch.objects.filter(id=request.data['id']).update(advisor=request.data['advisor'])
        return Response({"message": "Batch updated successfully"})
    else:
        return Response({"message": "You are not authorized to update Batch"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getGroups(request):
    if request.user.is_lead:
        groups = Group.objects.all()
        groupsArray = []
        for group in groups:
            group.student = Student.objects.filter(group=group)
            group.save()
            serializer = ViewGroupSerializer(group).data
            groupsArray.append(serializer)
        return Response(groupsArray)
    else:
        return Response({"message": "You are not authorized to view Group"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getMyGroups(request):
    if request.user.is_staff:
        groups = Group.objects.filter(advisor=request.user.advisor)
        groupsArray = []
        for group in groups:
            group.student = Student.objects.filter(group=group)
            group.save()
            serializer = ViewGroupSerializer(group).data
            groupsArray.append(serializer)
        return Response(groupsArray)
    else:
        return Response({"message": "You are not authorized to view Group"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getGroupLess(request):
    if request.user.is_lead:
        students = Student.objects.filter(group = None,domain__name=request.data['domain'], batch__name=request.data['batch'])
        for student in students:
            [student.week] = Manifest.objects.filter(student_name=student)[:1]
            student.week = student.week.title
            student.save()
        serializer = StudentGroupSerializer(students, many=True).data
        return Response(serializer)
    else:
        return Response({"message": "You are not authorized to view Group"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getGroupDetails(request):
    if request.user.is_lead:
        group = Group.objects.get(id=request.data['id'])
        group.student = Student.objects.filter(group=group)
        for student in group.student:
            [student.week] = Manifest.objects.filter(student_name=student)[:1]
            student.week = student.week.title
            student.save()
        group.save()
        serializer = ViewGroupDetailsSerializer(group).data
        return Response(serializer)
    else:
        return Response({"message": "You are not authorized to view Group"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getMyGroupDetails(request):
    if request.user.is_staff:
        group = Group.objects.get(id=request.data['id'])
        students = Student.objects.filter(group=group)
        for student in students:
            student.week = Manifest.objects.filter(student_name=student).order_by('-id')[0].title
            student.pending = Tasks.objects.filter(week__student_name=student, status=False).count()
            student.count = Review.objects.filter(manifest__student_name=student).count()
            student.save()
        serializer = GroupStudentDetailsSerializer(students, many=True).data
        return Response(serializer)
    else:
        return Response({"message": "You are not authorized to view Group"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addInGroup(request):
    if request.user.is_lead:
        student = Student.objects.get(id=request.data['student'])
        group = Group.objects.get(id=request.data['group'])
        student.group = group
        student.save()
        return Response({"message": "Student added in group successfully"})
    else:
        return Response({"message": "You are not authorized to add Student in Group"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def removeFromGroup(request):
    if request.user.is_lead:
        student = Student.objects.get(id=request.data['student'])
        student.group = None
        student.save()
        return Response({"message": "Student removed from group successfully"})
    else:
        return Response({"message": "You are not authorized to remove Student from Group"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createGroup(request):
    if request.user.is_lead:
        Group.objects.create( name = request.data['name'], batch = Batch.objects.get(id=request.data['batch']),
         domain = Domain.objects.get(id=request.data['domain']), advisor = Advisor.objects.get(id=request.data['advisor']))
        return Response({"message": "Group created successfully"})
    else:
        return Response({"message": "You are not authorized to create Group"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteGroup(request):
    if request.user.is_lead:
        Group.objects.filter(id=request.data['id']).delete()
        return Response({"message": "Group deleted successfully"})
    else:
        return Response({"message": "You are not authorized to delete Group"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateGroup(request):
    if request.user.is_lead:
        if request.data['advisor'] != '':
            Group.objects.filter(id=request.data['id']).update(name = request.data['new_name'], advisor = Advisor.objects.get(id=request.data['advisor']))
        else:
            Group.objects.filter(id=request.data['id']).update(name = request.data['new_name'])
        return Response({"message": "Group updated successfully"})
    else:
        return Response({"message": "You are not authorized to update Group"})
        