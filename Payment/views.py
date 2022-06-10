from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import datetime
from .models import Payment
from .serializer import PaymentSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rentPayments(request):
    if request.user.is_student:
        date = datetime.date.today()
        month = date.strftime("%B")
        pay = Payment.objects.filter(student=request.user.student,month=month,types='Rent', status='Pending')
        if pay:
            if pay[0].status == 'Pending':
                context = {
                    'id':pay[0].id,
                    'amount':pay[0].totalamt,
                    'type':pay[0].types,
                    'status':pay[0].status,
                    }
                return Response(context)
            elif pay[0].status == 'Partially':
                context = {
                    'id':pay[0].id,
                    'amount':pay[0].amount,
                    'type':pay[0].types,
                    'status':pay[0].status,
                    }
                return Response(context)
        else:
            if date.day <= 3:
                user = request.user
                student = user.student
                count = student.manifest_set.all().count() 
                
                if count >= 20:
                    amount = 3600
                elif count >= 21:
                    amount = 2800
                elif count >= 22:
                    amount = 2000
                elif count >= 23:
                    amount = 1200
                elif count >= 24:
                    amount = 500
                else:
                    amount = 4000
                pay = Payment.objects.create(student=student,totalamt=amount,types='Rent',status='Pending',month=month)
                context = {
                    'id':pay.id,
                    
                    'amount':pay.totalamt,
                    'type':pay.types,
                    'status':pay.status,
                }
                return Response(context)
            else:
                return Response({'status':'Paid'})
    
            
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def upfrontPayments(request):
    if request.user.is_student:
        date = datetime.date.today()
        month = date.strftime("%B")
        date_joined = int(request.user.date_joined.strftime("%d"))
        
        pay = Payment.objects.filter(student=request.user.student,month=month,types='Upfront')
        if pay:
            if pay[0].status == 'Pending':
                context = {
                    'id':pay[0].id,
                    'amount':pay[0].totalamt,
                    'type':pay[0].types,
                    'status':pay[0].status,
                    }
                return Response(context)
            elif pay[0].status == 'Partially':
                context = {
                    'id':pay[0].id,
                    'amount':pay[0].amount,
                    'paid':pay[0].amount,
                    'type':pay[0].types,
                    'status':pay[0].status,
                    }
                return Response(context)
            else:
                return Response({'status':'Paid'})
            
        else:
            print("Date joined",date_joined+3)
            print("today",date.day)
            print("expiry",date_joined+14)
            
            if date.day >= date_joined+3 and date.day <= date_joined+14:
                count = Payment.objects.filter(student=request.user.student,types='Upfront').count()
                print("count",count)
                user = request.user
                student = user.student
                if count == 0:
                    amount = 24500
                elif count == 1:
                    amount = 17500
                elif count == 2:
                    amount = 9000
                else:
                    return Response({'status':'Paid'})
                    
                pay = Payment.objects.create(student=student,totalamt=amount,types='Upfront',status='Pending',month=month)
                context = {
                    'id':pay.id,
                    'amount':pay.totalamt,
                    'type':pay.types,
                    'status':pay.status,
                }
                return Response(context)
            else:
                return Response({'status':'Paid'})
            
                
            
            
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def shiftPayments(request):
    if request.user.is_student:
        pay = Payment.objects.filter(student=request.user.student,types='BatchShift')
        if pay:
            if pay[0].status == 'Pending':
                context = {
                    'id':pay[0].id,
                    'amount':pay[0].totalamt,
                    'type':pay[0].types,
                    'status':pay[0].status,
                    }
                return Response(context)
        
            elif pay[0].status == 'Partially':
                context = {
                    'id':pay[0].id,
                    'amount':pay[0].amount,
                    'paid':pay[0].amount,
                    'type':pay[0].types,
                    'status':pay[0].status,
                    }
                return Response(context)
            
            else:
                return Response({'status':'Paid'})
        else:
            return Response({'status':'Paid'})
            
        
        
            
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def paying(request):
    print("Im here")
    if request.user.is_student:
        print("I am student")
        ids=request.data['id']
        types=request.data['type']
        amount = request.data['amount']
        date = datetime.date.today()
        month = date.strftime("%B")
        pay = Payment.objects.filter(id=ids,student=request.user.student,types=types,month=month)
        if pay:
            if pay[0].totalamt == amount:
                pay[0].paid=amount
                pay[0].status = 'Completed'
                pay[0].amount = amount
                pay[0].upi = amount
                pay[0].cash = 0
                pay[0].save()
                return Response({'status':'Paid'})
            elif pay[0].totalamt > amount:
                pay[0].status = 'Partially'
                pay[0].paid = amount
                pay[0].amount = pay[0].totalamt-amount
                pay[0].save()
                return Response({'status':'Partially'})
            
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myPayments(request):
    if request.user.is_student:
        payments= PaymentSerializer(Payment.objects.filter(student=request.user.student,status="Completed"),many=True).data
        return Response(payments)
    
        

        
        