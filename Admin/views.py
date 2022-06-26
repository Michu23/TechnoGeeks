from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Batch.models import Batch, Group
from User.models import User
from .models import Advisor, Reviewer, Code
from .serializer import AdvisorFullSerealizer, AdvisorHalfSerializer, ReviewerSerializer, CodeSerializer
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
        code = Code.objects.all()[0]
        code_serializer = CodeSerializer(code).data
        return Response({"advisors":advisors_serializer.data,"link":code_serializer})
    else:
        return Response({"message": "You are not authorized to get Advisors"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteAdvisor(request):
    if request.user.is_lead:
        advisor = Advisor.objects.filter(id=request.data['id'])
        User.objects.filter(advisor=advisor[0]).update(is_staff=False)
        return Response({"message": "Advisor deleted successfully"})
    else:
        return Response({"message": "You are not authorized to get Advisors"})