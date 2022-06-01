from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Batch.models import Batch
from Batch.models import Group
from .models import Advisor, Reviewer
from .serializer import AdvisorFullSerealizer, AdvisorHalfSerializer, ReviewerSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getAdvisorsNames(request):
    if request.user.is_lead:
        advisors = AdvisorHalfSerializer(Advisor.objects.all(), many=True)
        return Response(advisors.data)
    else:
        return Response({"message": "You are not authorized to get Advisors"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getReviewers(request):
    if request.user.is_lead or request.user.is_staff:
        reviewers = ReviewerSerializer(Reviewer.objects.all(), many=True)
        return Response(reviewers.data)
    else:
        return Response({"message": "You are not authorized to get Advisors"})
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getAdvisors(request):
    if request.user.is_lead:
        advisors = Advisor.objects.all()
        for advisor in advisors:
            advisor.batch = [ batch.name for batch in list(Batch.objects.filter(advisor=advisor))]
            advisor.group = Group.objects.filter(advisor=advisor)
            advisor.save()
        advisors_serializer = AdvisorFullSerealizer(advisors, many=True)
        return Response(advisors_serializer.data)
    else:
        return Response({"message": "You are not authorized to get Advisors"})