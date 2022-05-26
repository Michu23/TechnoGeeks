from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Batch.models import Batch
from Batch.models import Group
from .models import Advisor
from .serializer import AdvisorFullSerealizer, AdvisorHalfSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getAdvisorsNames(request):
    if request.user.is_lead:
        advisors = AdvisorHalfSerializer(Advisor.objects.all(), many=True)
        print(advisors.data)
        return Response(advisors.data)
    else:
        return Response({"message": "You are not authorized to get Advisors"})
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getAdvisors(request):
    if request.user.is_lead:
        advisors = Advisor.objects.all()
        for advisor in advisors:
            advisor.batch = [ x.batchno for x in list(Batch.objects.filter(advisor=advisor))]
            # advisor.batch = list(Batch.objects.filter(advisor=advisor))
            # a = [ x.batchno for x in list(Batch.objects.filter(advisor=advisor))]
            # print('a######################', a)
            advisor.group = Group.objects.filter(advisor=advisor)
        advisors_serializer = AdvisorFullSerealizer(advisors, many=True)
        print('1234567890-=======',advisors_serializer.data)
        return Response(advisors_serializer.data)
    else:
        return Response({"message": "You are not authorized to get Advisors"})