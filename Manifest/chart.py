import random
from datetime import datetime, date, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg, Sum, Count

from Student.models import Placement, Student
from Payment.models import Payment
from User.models import Domain
from .models import Manifest, Review

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getChartdata(request):
    if request.user.is_student:
        student = request.user.student
        manifests = Manifest.objects.filter(student_name=student, is_complete=True).order_by('id')
        chartData = [
            # this is the data of technical score for the student
            {"data":{
                "labels": [manifest.title for manifest in manifests],
                "title":"Technical workout",
                "data": [
                    {"backgroundColor":'rgb(255, 99, 132)', 
                    "borderColor": 'rgba(255, 99, 132, 1)', 
                    "data":[manifest.technical_score for manifest in manifests]},
                    ]},
            "type":"line"},
            # this is the data of personal score for the student
            {"data":{
                "labels": [manifest.title for manifest in manifests],
                "title":"Personal workout",
                "data": [
                    {"backgroundColor":'rgb(255, 99, 132)', 
                    "borderColor": 'rgba(255, 99, 132, 1)', 
                    "data":[manifest.misc_score for manifest in manifests]},
                    ]},
            "type":"line"}]
        return Response(chartData)
    elif request.user.is_staff and request.user.is_superuser == False:
        chartData = []
        advisor = request.user.advisor
        reviews = Review.objects.filter(advisor=advisor)
        chartData.append(
                # this is the data of count of on going students for each domain
                {"data":
                    {"labels": [day.strftime("%A") for day in getDays(7)],
                    "title":"By Day",
                    "data": [
                        {"label":"You", "data": [reviews.filter(created=day).count() for day in getDays(7)],
                        "backgroundColor": colorCreater("0.4"),
                        "borderColor": colorCreater("1")}],
                    "brWidth": 1},
                "type":"line"})
        chartData.append(
                # this is the data of count of on going students for each domain
                {"data":
                    {"labels": [week[0].strftime("%d/%m")+"-"+week[1].strftime("%d/%m") for week in getWeeks(6)],
                    "title":"By Week",
                    "data": [
                        {"label":"You", "data": [reviews.filter(created__in=week).count() for week in getWeeks(6)],
                        "backgroundColor": colorCreater("0.4"),
                        "borderColor": colorCreater("1")}],
                    "brWidth": 1},
                "type":"line"})
        chartData.append(
                # this is the data of count of on going students for each domain
                {"data":
                    {"labels": [month.strftime("%B") for month in getMonths(6)],
                    "title":"By Month",
                    "data": [
                        {"label":"You", "data": [reviews.filter(created=month).count() for month in getMonths(6)],
                        "backgroundColor": colorCreater("0.4"),
                        "borderColor": colorCreater("1")}],
                    "brWidth": 1},
                "type":"line"})
        return Response(chartData)
    elif request.user.is_lead:
        chartData = []
        if request.user.department.name == "Lead":
            domains = Domain.objects.all()
            onGoing = []
            overall = []
            onGoingBg = []
            onGoingBr = []
            overallBg = []
            overallBr = []
            for domain in domains:
                students = Student.objects.filter(domain=domain)
                overall.append(students.count())
                onGoing.append(students.filter(status="Training").count())
                onGoingBg.append(colorCreater("0.4"))
                onGoingBr.append(colorCreater("1"))
                overallBg.append(colorCreater("0.4"))
                overallBr.append(colorCreater("1"))
            chartData.append(
                # this is the data of count of on going students for each domain
                {"data":
                    {"labels": [domain.name for domain in domains],
                    "label":"On Going",
                    "data": onGoing,
                    "bgColor": onGoingBg,
                    "brColor": onGoingBr,
                    "brWidth": 1},
                "type":"doughnut"})
            chartData.append(
                # this is the data of count of overall students for each domain
                {"data":
                    {"labels": [domain.name for domain in domains],
                    "label":"Overall",
                    "data": overall,
                    "bgColor": overallBg,
                    "brColor": overallBr,
                    "brWidth": 1},
                "type":"doughnut"})
        if request.user.department.name == "Placement" or request.user.department.name == "Lead":
            now = datetime.now()
            months = [now]
            for _ in range(0, 5):
                now = now.replace(day=1) - timedelta(days=1)
                months.append(now)
            placemnts = Placement.objects.filter(
                created__lte=date.today(),
                created__gte=now.date().replace(day=int(datetime.today().strftime("%d"))))
            domains = Domain.objects.all()
            chartData.append(
                # this is the data of count of placemnts students for each month
                {"data":
                    {"labels": [month.strftime("%B") for month in months],
                    "title":"Placed",
                    "data": [
                        {"label":domain.name, "data": [placemnts.filter(created__month=month.strftime("%m"),
                        student__domain__name=domain.name).count() for month in months],
                        "backgroundColor": colorCreater("0.4"),
                        "borderColor": colorCreater("1")} for domain in domains],
                    "brWidth": 1},
                "type":"line"})
            chartData.append(
                # this is the data of average LPA of placemnts students for each month
                {"data":
                    {"labels": [month.strftime("%B") for month in months],
                    "title":"Placed",
                    "data": [
                        {"label":domain.name, 
                        "data": [toInt(placemnts.filter(created__month=month.strftime("%m"),
                            student__domain__name=domain.name).aggregate(Avg('LPA'))["LPA__avg"]) for month in months],
                        "backgroundColor": colorCreater("0.4"),
                        "borderColor": colorCreater("1")} for domain in domains],
                    "brWidth": 1},
                "type":"line"})
            chartData.append(
                # this is the data of LPA of placemnts students in each domain
                {"data":
                    {"labels": [domain.name for domain in domains],
                    "title":"LPA for each domain",
                    "data": [
                        {"label": "LPA", 
                        "backgroundColor": colorCreater("1"),
                         "borderColor": colorCreater("1"),
                         "data":[toInt(placemnts.filter(student__domain__name=domain.name).aggregate(Sum('LPA'))["LPA__sum"]) for domain in domains]},
                        ],
                    "brWidth": 1},
                "type":"bar"})
            chartData.append(
                # this is the data of LPA of placemnts students in each domain
                {"data":
                    {"labels": [placemnt.location for placemnt in placemnts.distinct('location')],
                    "title":"Count for each Location",
                    "data": [
                        {"label": "LPA", 
                        "backgroundColor": colorCreater("1"),
                         "borderColor": colorCreater("1"),
                         "data":[placemnts.filter(location=placemnt.location).count() for placemnt in placemnts.distinct('location')]},
                        ],
                    "brWidth": 1},
                "type":"bar"})
        if request.user.department.name == "Finance" or request.user.department.name == "Lead":
            now = datetime.now()
            months = getMonths(6)
            domains = Domain.objects.all()
            R_reviews = Review.objects.values('reviewer__name').annotate(count=Count('reviewer__name')).order_by('-count')[:10]
            A_reviews = Review.objects.values('advisor__user__username').annotate(count=Count('advisor__user__username')).order_by('-count')[:10]
            S_reviews = Review.objects.values('manifest__student_name__user__username').annotate(count=Count('manifest__student_name__user__username')).order_by('-count')[:10]
            students = Student.objects.filter(status="Training")
            payments = Payment.objects.filter(month=now.strftime("%B"), types__in=['Upfront', 'Rent'])
            upfront_cash = payments.filter(types='Upfront').aggregate(Sum('cash'))['cash__sum']
            upfront_upi = payments.filter(types='Upfront').aggregate(Sum('upi'))['upi__sum']
            rent_cash = payments.filter(types='Rent').aggregate(Sum('cash'))['cash__sum']
            rent_upi = payments.filter(types='Rent').aggregate(Sum('upi'))['upi__sum']
            upfront = (upfront_cash if upfront_cash is not None else 0) + (upfront_upi if upfront_upi is not None else 0)
            rent = (rent_cash if rent_cash is not None else 0) + (rent_upi if rent_upi is not None else 0)
            chartData.append(
                # this is the data of count of overall students for each domain
                {"data":
                    {"labels": ["Upfront", "ISI"],
                    "label":"Count of Upfront and ISI",
                    "data": [students.filter(fee="Upfront").count(), students.filter(fee="ISI").count()],
                    "bgColor": [colorCreater('0.4'), colorCreater('0.4')],
                    # "brColor": [colorCreater('1'), colorCreater('1')],
                    "brWidth": 1},
                "type":"pie"})
            chartData.append(
                # this is the data of count of overall students for each domain
                {"data":
                    {"labels": ["Rent", "Upfront"],
                    "label":"Total Rent and Upfront of this month",
                    "data": [rent, upfront],
                    "bgColor": [colorCreater('0.4'), colorCreater('0.4')],
                    # "brColor": [colorCreater('1'), colorCreater('1')],
                    "brWidth": 1},
                "type":"pie"})
            chartData.append(
                # this is the data of review count of reviewers 
                {"data":
                    {"labels": [month.strftime("%B") for month in months],
                    "title":"Review count of each Reviewer",
                    "data": [
                        {"label": review["reviewer__name"],
                        "data": [Review.objects.filter(reviewer__name=review["reviewer__name"], 
                            created__month=month.strftime("%m")).count() for month in months],
                        "backgroundColor": colorCreater("0.4"),
                        "borderColor": colorCreater("1")} for review in R_reviews],
                    "brWidth": 1},
                "type":"line"})
            chartData.append(
                # this is the data of review count of advisors 
                {"data":
                    {"labels": [month.strftime("%B") for month in months],
                    "title":"Review count of each Advisor",
                    "data": [
                        {"label": review["advisor__user__username"],
                        "data": [Review.objects.filter(advisor__user__username=review["advisor__user__username"], 
                            created__month=month.strftime("%m")).count() for month in months],
                        "backgroundColor": colorCreater("0.4"),
                        "borderColor": colorCreater("1")} for review in A_reviews],
                    "brWidth": 1},
                "type":"line"})
            chartData.append(
                # this is the data of review count of advisors 
                {"data":
                    {"labels": [month.strftime("%B") for month in months],
                    "title":"Review count of each Student",
                    "data": [
                        {"label": review["manifest__student_name__user__username"],
                        "data": [Review.objects.filter(manifest__student_name__user__username=review["manifest__student_name__user__username"], 
                            created__month=month.strftime("%m")).count() for month in months],
                        "backgroundColor": colorCreater("0.4"),
                        "borderColor": colorCreater("1")} for review in S_reviews],
                    "brWidth": 1},
                "type":"line"})
        return Response(chartData)
    else:
        return Response({'error': 'You are not allowed to perform this action'})

def toInt(num):
    if num is None:
        return 0
    else:
        return int(num)
def colorCreater(opcity):
    color = [random.choice(range(240)) for i in range(3)]
    return "rgb("+str(color[0])+", "+str(color[1])+", "+str(color[2])+", "+opcity+")"

def getMonths(count):
    now = datetime.now()
    months = [now]
    for _ in range(0, int(count)-1):
        now = now.replace(day=1) - timedelta(days=1)
        months.append(now)
    return months

def getWeeks(count):
    now = datetime.now()
    weeks = []
    for _ in range(0, int(count)):
        weeks.append([now, now-timedelta(days=6)])
        now = now - timedelta(days=7)
    return weeks

def getDays(count):
    now = datetime.now()
    days = [now]
    for _ in range(0, int(count)-1):
        now = now - timedelta(days=1)
        days.append(now)
    return days