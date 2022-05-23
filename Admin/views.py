from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Advisor
from .serializer import AdvisorHalfSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getAdvisors(request):
    if request.user.is_lead:
        advisors = AdvisorHalfSerializer(Advisor.objects.all(), many=True)
        print(advisors.data)
        return Response(advisors.data)
    else:
        return Response({"message": "You are not authorized to get Advisors"})