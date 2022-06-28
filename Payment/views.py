import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import datetime
from .models import Payment
from .serializer import PaymentSerializer,OrderSerializer
from django.db.models import Q
from datetime import timedelta
import razorpay
client = razorpay.Client(auth=("rzp_test_KgiLdhTO6F4BS3", "XBUSNhYRLL2J6eODHO4aw18W"))


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rentPayments(request):
    if request.user.is_student:
        date = datetime.date.today()
        month = date.strftime("%B")
        pay = Payment.objects.filter(student=request.user.student,month=month,types='Rent')
        pay2 = Payment.objects.filter(student=request.user.student,types='Rent',status='Completed',month=month)
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
            
        if pay:
            if pay[0].status == 'Pending' or pay[0].status == 'Partially':
                if date.day>4 and date>pay[0].expiry_date:
                    pay[0].status = 'Expired'
                    pay[0].save()
            
            if pay[0].status == 'Pending' or pay[0].status == 'Partially':
                context = {
                    'id':pay[0].paymentid,
                    'amount':pay[0].amount,
                    'type':pay[0].types,
                    'status':pay[0].status,
                    }
                return Response(context)
            else:
                return Response({'status':'Paid'})
        elif date.day <= 3:
            rpay= client.order.create({
            "amount": amount*100,
            "currency": "INR",
            "partial_payment": True,
            "notes": {
                "Type": "Rent",
                "Student": student.user.username,
            }
            })
            pay = Payment.objects.create(student=student,amount=amount,totalamt=amount,types='Rent',status='Pending',month=month,paymentid=rpay['id'])
            context = {
                'id':pay.paymentid,
                'amount':pay.totalamt,
                'type':pay.types,
                'status':pay.status,
            }
            return Response(context)
        elif len(pay2) is 0:
            newrpay = client.order.create({
            "amount": amount*100,
            "currency": "INR",
            "partial_payment": True,
            "notes": {
                "Type": "Rent",
                "Student": student.user.username,
            }
            })
            newpay = Payment.objects.create(student=student,amount=amount,totalamt=amount,types='Rent',status='Expired',month=month,paymentid=newrpay['id'])
            context = {
                'id':newpay.paymentid,
                'amount':newpay.totalamt,
                'type':newpay.types,
                'status':newpay.status,
            }
            return Response(context)
        else:
            return Response({'status':'Paid'})
            
    
            
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def upfrontPayments(request):
    if request.user.is_student and request.user.student.fee=="Upfront":
        date = datetime.datetime.today()
        date_2 = datetime.date.today()
        month = date.strftime("%B")
        date_joined = request.user.date_joined
        start = date_joined+timedelta(3)
        expiry = date_joined+timedelta(6)

        pay = Payment.objects.filter(student=request.user.student,month=month,types='Upfront')
        if pay:
            if pay[0].status == 'Pending' or pay[0].status == 'Partially':
                if date.replace(tzinfo=None) >= expiry.replace(tzinfo=None):
                    if date_2>pay[0].expiry_date:
                        pay[0].status = 'Expired'
                        pay[0].save()
                        
            if pay[0].status == 'Pending' or pay[0].status == 'Partially':
                context = {
                    'id':pay[0].paymentid,
                    'amount':pay[0].amount,
                    'type':pay[0].types,
                    'status':pay[0].status,
                    }
                return Response(context)
            else:
                return Response({'status':'Paid'})
            
        else:
            
            if date.day >= start.day and date.day <= expiry.day:
                count = Payment.objects.filter(student=request.user.student,types='Upfront').count()
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

                rpay= client.order.create({
                "amount": amount*100,
                "currency": "INR",
                "partial_payment": True,
                "notes": {
                    "Type": "Upfront",
                    "Student": student.user.username,
                }
                })
                    
                pay = Payment.objects.create(student=student,totalamt=amount,amount=amount,types='Upfront',status='Pending',month=month,expiry_date=expiry,paymentid=rpay['id'])
                context = {
                    'id':pay.paymentid,
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
        date = datetime.date.today()
        pay = Payment.objects.filter(student=request.user.student,types='BatchShift')
        if pay:
            if pay[0].status == 'Pending' or pay[0].status == 'Partially':
                if date>pay[0].expiry_date:
                    pay[0].status = 'Expired'
                    pay[0].save()
                else:
                    pass
            else:
                pass
            if pay[0].status == 'Pending' or pay[0].status == 'Partially':

                context = {
                    'id':pay[0].paymentid,
                    'amount':pay[0].amount,
                    'type':pay[0].types,
                    'status':pay[0].status,
                    }
                return Response(context)
            else:
                return Response({'status':'Paid'})
        else:
            return Response({'status':'Paid'})
            
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def FinePayments(request):
    if request.user.is_student:
        date = datetime.date.today()
        pay = Payment.objects.filter(types="Fine").order_by('-id')
        if pay:
            if pay[0].status == 'Pending' or pay[0].status == 'Partially':
                if date>pay[0].expiry_date:
                    pay[0].status = 'Expired'
                    pay[0].save()
                
            if pay[0].status == 'Pending' or pay[0].status == 'Partially':
                context = {
                    'id':pay[0].paymentid,
                    'amount':pay[0].totalamt,
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
def start_payment(request):

    print(request.data)
    amount = request.data['amount']
    theid = request.data['id']
    
    payment=client.order.fetch(theid)

    # we are saving an order with isPaid=False
    order = Payment.objects.get(paymentid=theid)

    serializer = OrderSerializer(order)

    data = {
        "payment": payment,
        "order": serializer.data
    }
    return Response(data)
            
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def paying(request):
    if request.user.is_student:
        res = json.loads(request.data["response"])
        print(res)

        ord_id = ""
        raz_pay_id = ""
        raz_signature = ""

        # res.keys() will give us list of keys in res
        for key in res.keys():
            if key == 'razorpay_order_id':
                ord_id = res[key]
            elif key == 'razorpay_payment_id':
                raz_pay_id = res[key]
            elif key == 'razorpay_signature':
                raz_signature = res[key]

        date = datetime.date.today()
        pay = Payment.objects.get(paymentid=ord_id)
        data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
        }
        print(data)

        client = razorpay.Client(auth=("rzp_test_KgiLdhTO6F4BS3", "XBUSNhYRLL2J6eODHO4aw18W"))
        check = client.utility.verify_payment_signature(data)
        print(check)

        payment = client.order.fetch(ord_id)
        print(payment['amount'])
        
        if check and pay.status is not 'Completed':
            if  payment['amount'] == payment['amount_paid']:
                pay.paid=payment['amount']/100
                pay.status = 'Completed'
                pay.amount = payment['amount_due']/100
                pay.upi = payment['amount']
                pay.cash = 0
                pay.paid_date= date
                pay.save()
                return Response({'status':'Paid'})

            elif payment['amount'] > payment['amount_paid']:
                pay.status = 'Partially'
                pay.paid =payment['amount_paid']/100
                pay.amount = payment['amount_due']/100
                pay.save()
                return Response({'status':'Partially'})

        else:
            return Response({'status':'Failed'})
            
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
        pay = Payment.objects.filter(paymentid=ids)
        if pay:
            pay[0].paid=pay[0].paid + pay[0].amount
            pay[0].status = 'Completed'
            pay[0].cash = pay[0].cash + pay[0].amount
            pay[0].amount = 0
            pay[0].paid_date= date
            pay[0].save()
            return Response({'status':'Paid'})
        
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendForm(request):
    if request.user.is_lead:
        ids = request.data['id']
        amount = request.data['amount']
        print(ids)
        next_day = datetime.datetime.now()+timedelta(1)
        date = datetime.date.today()
        month = date.strftime("%B")
        pay = Payment.objects.get(id=ids)

        lastpay = Payment.objects.filter(student=pay.student,types="Fine").order_by('-id')

        if lastpay:
            if lastpay[0].month and amount!=0:
                rpay= client.order.create({
                    "amount": int(amount)*100,
                    "currency": "INR",
                    "partial_payment": True,
                    "notes": {
                        "Type": "Fine",
                        "Student": pay.student.user.username,
                    }
                    })
                        
                newpay = Payment.objects.create(student=pay.student,totalamt=amount,amount=amount,types='Fine',status='Pending',month=month,expiry_date=next_day,paymentid=rpay['id'])
          
        elif amount!=0:
            rpay= client.order.create({
                "amount": int(amount)*100,
                "currency": "INR",
                "partial_payment": True,
                "notes": {
                    "Type": "Fine",
                    "Student": pay.student.user.username,
                }
                })  
            newpay = Payment.objects.create(student=pay.student,totalamt=amount,amount=amount,types='Fine',status='Pending',month=month,expiry_date=next_day,paymentid=rpay['id'])
                
        if pay:
            if pay.status == 'Expired':
                if pay.paid == 0:
                    pay.status = 'Pending'
                    pay.expiry_date = next_day
                    pay.save()
                else:
                    pay.status = 'Partially'
                    pay.expiry_date = next_day
                    pay.save()
                return Response({'status':'Success'})
        else :
            return Response({'status':'Not Found'})
    else:
        return Response({'status':'Not Authorized'})
            
        
    

        

        
        