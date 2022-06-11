from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import datetime
from .models import Payment
from .serializer import PaymentSerializer
from django.db.models import Q

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rentPayments(request):
    if request.user.is_student:
        date = datetime.date.today()
        month = date.strftime("%B")
        pay = Payment.objects.filter(student=request.user.student,month=month,types='Rent')
        if pay:
            if pay[0].status == 'Pending':
                print("Pending")
                context = {
                    'id':pay[0].id,
                    'amount':pay[0].totalamt,
                    'type':pay[0].types,
                    'status':pay[0].status,
                    }
                return Response(context)
            elif pay[0].status == 'Partially':
                print("Partially")
                context = {
                    'id':pay[0].id,
                    'amount':pay[0].amount,
                    'type':pay[0].types,
                    'status':pay[0].status,
                    }
                return Response(context)
            else:
                print("Completed")
                return Response({'status':'Paid'})
        else:
            if date.day <= 11:
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
                pay = Payment.objects.create(student=student,amount=amount,totalamt=amount,types='Rent',status='Pending',month=month)
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
                    
                pay = Payment.objects.create(student=student,totalamt=amount,amount=amount,types='Upfront',status='Pending',month=month)
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
    if request.user.is_student:
        ids=request.data['id']
        types=request.data['type']
        amount = int(request.data['amount'])
        date = datetime.date.today()
        month = date.strftime("%B")
        pay = Payment.objects.filter(id=ids,student=request.user.student,types=types,month=month)
        if pay:
            if pay[0].amount == amount:
                pay[0].paid=amount
                pay[0].status = 'Completed'
                pay[0].amount = pay[0].amount - amount
                pay[0].upi = amount
                pay[0].cash = 0
                pay[0].paid_date= date
                pay[0].save()
                return Response({'status':'Paid'})
            elif pay[0].amount > amount:
                pay[0].status = 'Partially'
                pay[0].paid =pay[0].paid + amount
                pay[0].amount = pay[0].totalamt-pay[0].paid
                pay[0].save()
                return Response({'status':'Partially'})
            
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myPayments(request):
    if request.user.is_student:
        payments= PaymentSerializer(Payment.objects.filter(Q(status="Completed") | Q(status="Expired"), student=request.user.student).order_by('-status'),many=True).data
        return Response(payments)
    else:
        return Response({'status':'Not Student'})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allCompletedPayments(request):
    if request.user.is_lead:
        payments= PaymentSerializer(Payment.objects.filter(status="Completed"),many=True).data
        return Response(payments)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allPendingPayments(request):
    if request.user.is_lead:
        payments= PaymentSerializer(Payment.objects.filter(Q(status="Partially") | Q(status="Pending") | Q(status="Expired")),many=True).data
        return Response(payments)
    else:
        return Response({'status':'Not Authorized'})
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cashPaid(request):
    if request.user.is_lead:
        ids = request.data['id']
        date = datetime.date.today()
        pay = Payment.objects.filter(id=ids)
        if pay:
            pay[0].paid=pay[0].paid + pay[0].amount
            pay[0].status = 'Completed'
            pay[0].cash = pay[0].cash + pay[0].amount
            pay[0].amount = 0
            pay[0].paid_date= date
            pay[0].save()
            return Response({'status':'Paid'})
        
from datetime import timedelta
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendForm(request):
    if request.user.is_lead:
        ids = request.data['id']
        next_day = datetime.datetime.now()+timedelta(1)
        date = datetime.date.today()
        pay = Payment.objects.filter(id=ids)
        if pay:
            if pay[0].status == 'Expired':
                pay[0].status = 'Pending'
                pay[0].expiry_date = next_day
                pay[0].save()
                return Response({'status':'Success'})
        else :
            return Response({'status':'Not Found'})
    else:
        return Response({'status':'Not Authorized'})
            
        
    

        

        
        