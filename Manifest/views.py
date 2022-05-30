from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Review, Student, Tasks
from .serializer import StudentTasklistSerializer, ManifestTaskSerealizer
from Manifest.models import Manifest


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getTaskslist(request):
    if request.user.is_staff:
        student = Student.objects.get(id=request.data['id'])
        manifests = Manifest.objects.filter(student_name=student)
        for manifest in manifests:
            manifest.pending = Tasks.objects.filter(week=manifest, status=False).count()
            manifest.reviews = Review.objects.filter(manifest=manifest)
            manifest.save()
        serializer = StudentTasklistSerializer(manifests, many=True).data
        return Response(serializer)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getManifest(request):
    if request.user.is_staff:
        manifest = Manifest.objects.get(id=request.data['id'])
        manifest.tasks = Tasks.objects.filter(week=manifest)
        serializer = ManifestTaskSerealizer(manifest).data
        return Response(serializer)