from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Student.models import Placement, Student
from .models import Batch, Group
from Admin.models import Advisor
from User.models import Domain
from .serializer import ViewBatchSerializer, ViewGroupSerializer
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getBatch(request):
    if request.user.is_lead:
        batchs = Batch.objects.all()
        batchsArray = []
        for batch in batchs:
            batch.placement = Placement.objects.filter(student__batch=batch)
            batch.student = Student.objects.filter(batch=batch)
            batch.save()
            serializer = ViewBatchSerializer(batch).data
            batchsArray.append(serializer)
        print(batchsArray)
        return Response(batchsArray)
    else:
        return Response({"message": "You are not authorized to view Batch"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createBatch(request):
    if request.user.is_lead:
        advisor = Advisor.objects.get(id=request.data['advisor'])
        Batch.objects.create( batchno=request.data['batchno'], advisor=advisor, location=request.data['location'])
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
        Batch.objects.filter(id=request.data['id']).update(advisor=request.data['advisor'], location=request.data['location'])
        return Response({"message": "Batch updated successfully"})
    else:
        return Response({"message": "You are not authorized to update Batch"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getGroup(request):
    if request.user.is_lead:
        groups = Group.objects.all()
        groupsArray = []
        for group in groups:
            group.student = Student.objects.filter(group=group)
            group.save()
            serializer = ViewGroupSerializer(group).data
            groupsArray.append(serializer)
        print(groupsArray)
        return Response(groupsArray)
    else:
        return Response({"message": "You are not authorized to view Group"})

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
        Group.objects.filter(id=request.data['id']).update(name = request.data['name'], batch = Batch.objects.get(id=request.data['batch']),
         domain = Domain.objects.get(id=request.data['domain']), advisor = Advisor.objects.get(id=request.data['advisor']))
        return Response({"message": "Group updated successfully"})
    else:
        return Response({"message": "You are not authorized to update Group"})