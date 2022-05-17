from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createBatch(request):
    if request.user.is_lead:
        Batch.objects.create( batchno=request.data['batchno'], advisor=request.data['advisor'] )
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