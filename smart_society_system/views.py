from django.http.response import JsonResponse
from members.models import CommiteeMember
from members.models import Member
from transactions.models import Expense
from society_information.models import SocietyInformation
from complaints.models import Complaint
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render

class MemberLogin(View):
    def get(self,request):
        if request.user.id != None:
            return redirect("home")
        return render(request, 'user/login.html')
    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect("login")  

class MemberLogout(View):
    def get(self, request):
        logout(request)    
        return redirect('login')

class Home(View):
    def get(self,request):
        if request.user.id == None:
            return redirect("login")
        Member_details = Member.objects.all()
        context ={"Member_details": Member_details}
        return render(request, 'user/home.html', context)

def expenseData(request):
    if request.is_ajax() and request.method == 'GET':
        expenses = Expense.objects.values()
        list_result = [entry for entry in expenses]
        length = len(list_result)
        expenses_dates = []
        expenses_amounts = []
        for i in range(length-1,-1,-1):
            expenses_dates.append(list_result[i]["createdAt"].date())
            expenses_amounts.append(list_result[i]["amount"])
        return JsonResponse({"expenses_dates": expenses_dates, "expenses_amounts": expenses_amounts})


def societyInfoData(request):
    if request.is_ajax() and request.method =="GET":
        data = SocietyInformation.objects.values()
        list_result = [entry for entry in data]
        return  JsonResponse({"numberOfWings": list_result[0]["number_of_Wings"], "numberOfFlats" : list_result[0]["number_of_Flats"], "numberOfResidents":list_result[0]["number_of_Residents"], "numberOfTenants": list_result[0]["number_of_Tenants"]})


def commiteeMembersTabelData(request):
    if request.is_ajax() and request.method == "GET":
        CommiteeMembers = CommiteeMember.objects.all()
        list_result = []
        for Cmember in CommiteeMembers:
            list_result.append({"name":Cmember.member.first_name + " " + Cmember.member.last_name  ,"id":Cmember.member.id,"position":Cmember.position, "from_Date":Cmember.from_Date})
        
        # list_result = [entry for entry in CommiteeMembers]
        return JsonResponse({"commitee_members": list_result})


def complaintsData(request):
    if request.is_ajax() and request.method == "GET":
        complaints = Complaint.objects.all()
        pendingComplaints = 0
        activeComplaints = 0
        resolvedComplaints = 0
        for complain in complaints:
            if complain.status == "pending":
                pendingComplaints += 1
            elif complain.status == "active":
                activeComplaints += 1
            else:
                resolvedComplaints += 1
        return JsonResponse({"pendingComplaints":pendingComplaints, "activeComplaints":activeComplaints, "resolvedComplaints":resolvedComplaints})