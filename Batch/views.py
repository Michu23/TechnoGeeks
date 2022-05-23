from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Student.models import Placement, Student
from .models import *
from .serializer import ViewBatchSerializer
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