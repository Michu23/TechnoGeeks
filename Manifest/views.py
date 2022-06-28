from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from Admin.models import Reviewer, Advisor
from .models import Review, Student, Tasks
from .serializer import StudentTasklistSerializer, ManifestTaskSerealizer, TasksSerealizer
from Manifest.models import Manifest


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getTaskslist(request):
    if request.user.is_lead or request.user.is_staff or request.user.is_student:
        if request.user.is_lead or request.user.is_staff:
            student = Student.objects.get(id=request.data['id'])
        else:
            student = request.user.student
        manifests = Manifest.objects.filter(student_name=student).order_by('-id')
        for manifest in manifests:
            manifest.pending = Tasks.objects.filter(week=manifest, status=False).count()
            manifest.reviews = Review.objects.filter(manifest=manifest)
            manifest.save()
        serializer = StudentTasklistSerializer(manifests, many=True).data
        return Response(serializer)
    else:
        return Response({'error': 'You are not allowed to perform this action'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getManifest(request):
    if request.user.is_lead or request.user.is_staff or request.user.is_student:
        manifest = Manifest.objects.get(id=request.data['id'])
        manifest.tasks = Tasks.objects.filter(week=manifest)
        serializer = ManifestTaskSerealizer(manifest).data
        return Response(serializer)
    else:
        return Response({'error': 'You are not allowed to perform this action'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTask(request):
    if request.user.is_staff:
        print(request.data['manifest'])
        Tasks.objects.create(
            week=Manifest.objects.get(id=request.data['manifest']),
            taskname=request.data['task'],
            status=False
        )
        return Response({'success': 'Task added'})
    else:
        return Response({'error': 'You are not allowed to perform this action'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def completeTask(request):
    if request.user.is_staff:
        Tasks.objects.filter(id=request.data['task']).update(status=True)
        return Response({'success': 'Task completed'})
    else:
        return Response({'error': 'You are not allowed to perform this action'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reviewPassed(request):
    if request.user.is_staff:
        manifest = Manifest.objects.get(id=request.data['manifest'])
        Review.objects.create(
            manifest=manifest,
            advisor=Advisor.objects.get(user=request.user),
            reviewer=Reviewer.objects.get(id=request.data['reviewer']),
            remark=request.data['remark'],
            status=request.data['status'])
        manifest.is_complete = True
        manifest.personal_wo = request.data['form']['personal_wo']
        manifest.technical_score = request.data['form']['technical_score']
        manifest.misc_score = request.data['form']['misc_score']
        manifest.save()
        week_no = int(manifest.title[-2:]) + 1
        newName = "week 0" + str(week_no) if week_no < 10 else "week " + str(week_no)
        Manifest.objects.create(title=newName,
                                student_name=manifest.student_name,
                                next_review=request.data['next_review'])
        return Response({'success': 'Review passed'})
    else:
        return Response({'error': 'You are not allowed to perform this action'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reviewRepeated(request):
    if request.user.is_staff:
        manifest = Manifest.objects.get(id=request.data['manifest'])
        Review.objects.create(manifest=manifest,
            advisor=Advisor.objects.get(user=request.user),
            reviewer=Reviewer.objects.get(id=request.data['reviewer']),
            remark=request.data['remark'],
            status=request.data['status'])
        manifest.next_review = request.data['next_review']
        manifest.personal_wo = request.data['form']['personal_wo']
        manifest.technical_score = request.data['form']['technical_score']
        manifest.misc_score = request.data['form']['misc_score']
        manifest.save()
        return Response({'success': 'Review repeated'})
    else:
        return Response({'error': 'You are not allowed to perform this action'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getPendings(request):
    if request.user.is_staff or request.user.is_lead:
        student = Student.objects.get(id=request.data['id'])
    elif request.user.is_student:
        student = Student.objects.get(user=request.user)
    else:
        return Response({'error': 'You are not allowed to perform this action'})
    manifests = Manifest.objects.filter(student_name=student)
    pending = Tasks.objects.filter(week__in=manifests, status=False)
    serializer = TasksSerealizer(pending, many=True).data
    return Response(serializer)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deletePendings(request):
    if request.user.is_staff or request.user.is_lead:
        Tasks.objects.filter(id=request.data['id']).update(status=True)
        return Response({'success': 'Task deleted'})
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def folderSubmit(request):
    if request.user.is_student:
        Manifest.objects.filter(id=request.data['manifest']).update(folder=request.data['folder'])
        return Response({'success': 'Folder submitted'})
    else:
        return Response({'error': 'You are not allowed to perform this action'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_task(request):
    if request.user.is_staff:
        Tasks.objects.filter(id=request.data['id']).delete()
        return Response({'success': 'Task deleted'})
    else:
        return Response({'error': 'You are not allowed to perform this action'})

        