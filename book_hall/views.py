from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View
from .models import BookHall
from datetime import date, datetime
from django.contrib import messages
# Create your views here.

class HallApplications(View):
    def get(self, request):
        bookHallApplications = BookHall.objects.all()
        context = {"bookHallApplications": bookHallApplications}
        return render(request, "book_hall/book_hall.html", context)
class RegisterHall(View):
    def get(Self, request):
        return render(request, "book_hall/form.html")
    def post(self, request):
        name = request.POST.get("event_name")
        startTime = request.POST.get("start_time")
        endTime = request.POST.get("end_time")
        date = request.POST.get("date")
        if not name or not startTime or not endTime or not date:
            messages.error(request, "* Fields are mandatory")
            return redirect("register_hall")
        elif(checkForValidDate(date)):
            messages.error(request, "Date (" + date +") is not valid")
            return redirect("register_hall")
        elif(checkForValidStartEndTime(startTime,  endTime)):
            messages.error(request, "End time should be greater than start time")
            return redirect("register_hall")
        elif (chechForduplicateData(date, startTime, endTime, request)):
            messages.warning(request, "Hall is already booked for the date "+ date+ " and time "+startTime + " to "+ endTime)
            return redirect("register_hall")
        else:
            BookHall.objects.create(member=request.user, event_Name=name, date=date, start_Time=startTime, end_Time=endTime)
            messages.success(request, "Application registered successfully.")
            print("no....")
        return redirect("hall_applications")

class FilterHallApplication(View):
    def get(self, request, filterBy):
        if filterBy == "yours":
            filteredApplications = BookHall.objects.filter(member = request.user.id)
        elif filterBy == "all":
            filteredApplications = BookHall.objects.all()
        else:
            filteredApplications = BookHall.objects.filter(status=filterBy)
        context = {"bookHallApplications": filteredApplications}
        return render(request, "book_hall/book_hall.html", context)


def checkForValidDate(date):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    if(date < datetime.today().date()):
        return True
    return False

def checkForValidStartEndTime(startTime, endTime):
    start_time = datetime.strptime(startTime, "%H:%M")
    a_timedelta = start_time - datetime(1900, 1, 1)
    end_time = datetime.strptime(endTime, "%H:%M")
    b_timedelta = end_time - datetime(1900, 1, 1)
    if(a_timedelta.total_seconds() > b_timedelta.total_seconds()):
        return True;
    return False

def chechForduplicateData(date, startTime, endTime, request):
    old_applications = BookHall.objects.filter(date=date)
    start_time = datetime.strptime(startTime, "%H:%M").time()
    print(type(start_time))
    for application in old_applications:
        print(type(application.start_Time))
        if start_time >= application.start_Time and start_time <= application.end_Time:
            return True
    return False