from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import datetime
from .models import Payment

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rentPayment(request):
    m=0
    paid=0
    if request.user.is_student:
        date= datetime.datetime.now()
        month = date.strftime("%m")
        
        
        pay = Payment.objects.filter(student=request.user.student, types='Rent',date__month=date.month)[0]
        
        if date.day >= 3:
            if len(pay) is 0:
                paid = pay.amount
                user = request.user
                student = user.student
                count = student.manifest_set.all().count() 
                
                
                if count >= 20:
                    amount = 3600-paid
                    context={
                        'amount':amount,
                        'month':month,
                        'paid':paid,
                        'status':'Pending',
                    }
                    return Response(context)      
                
                if count >= 21:
                    amount = 2800-paid
                    context={
                        'amount':amount,
                        'month':month,
                        'paid':paid,
                        'status':'Pending',

                    }
                    return Response(context) 
                
                if count >= 22:
                    amount = 2000-paid
                    context={
                        'amount':amount,
                        'month':month,
                        'paid':paid,
                        'status':'Pending',

                    }
                    return Response(context) 
                
                if count >= 23:
                    amount = 1200-paid
                    context={
                        'amount':amount,
                        'month':month,
                        'paid':paid,
                        'status':'Pending',

                    }
                    return Response(context) 
                
                if count >= 24:
                    amount = 500-paid
                    context={
                        'amount':amount,
                        'month':month,
                        'paid':paid,
                        'status':'Pending',

                    }
                    return Response(context) 
                
                context={
                        'amount':4000-paid,
                        'month':month,
                        'paid':paid,
                        'status':'Pending',

                    }
                return Response(context) 
            
            else:
                return Response("Negative")
        else:
            return Response("Negative")
 
                
