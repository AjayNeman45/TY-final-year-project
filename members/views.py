from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MyChangeFormPassword, MemberEditForm
from complaints.forms import ComplaintCreateForm

from .models import CommiteeMember, Member
from transactions.models import Expense,Charges,Income
from complaints.models import Complaint
from meetings.models import Meeting
from events.models import Event
import json
from django.contrib.auth import update_session_auth_hash

class Profile(LoginRequiredMixin,View):
    def get(self,request): 
        member_obj = Member.objects.get(id=request.user.id)
        context = {'member':member_obj }
        return render(request, 'Members/profile.html',context) 


class Edit_Profile(LoginRequiredMixin,View):
    def get(self,request,**kwargs): 
        members = Member.objects.get(id=request.user.id)
        context = {'member':members,'id':request.user.id}
        return render(request, 'Members/edit_profile.html',context)  


    def post(self, request):
        post_data =  json.loads(request.body.decode("utf-8"))
        member = Member.objects.get(id = request.user.id)
        form = MemberEditForm(request.POST, request.files, instance=member)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, form.error_class)
            return JsonResponse({"status": False,"errors" : form.errors})
        return JsonResponse({"status": True})
       

class Change_Password(View):
    def get(self, request):
        instance_user = get_object_or_404(Member, id=request.user.id)
        form_edit_password = MyChangeFormPassword(instance_user)
        context={'form_edit_password': form_edit_password}
        return render(request, "Members/change_password.html", context)  
    def post(self, request):
        instance_user = get_object_or_404(Member, id=request.user.id)
        form_edit_password = MyChangeFormPassword(instance_user)
        form = MyChangeFormPassword(user=request.user, data=request.POST)
        if form.is_valid():
            messages.success(request, "Password Successfully Changed..")
            form.save()
            update_session_auth_hash(request, form.user)

        context = {'form_edit_password': form_edit_password, 'errors': form.errors}
        return render(request, "Members/change_password.html", context)  


class Society_Members_Information(View):
    def get(self,request,**kwargs):
        Member_details = Member.objects.all()
        context ={"member_details": Member_details,'id':request.user.id}
        return render(request, 'Members/society_member_info.html', context)

class Commitee_Members_Information(View):
    def get(self,request,**kwargs):
        commitee_details = CommiteeMember.objects.all()
        context = {"commitee_details":commitee_details,'id':request.user.id}
        return render(request,'Members/commitee_members_info.html' , context)

class Society_Expenses(View):
    def get(self,request,**kwargs):
        context ={'society_expenses':Expense.objects.all(),'id':request.user.id}
        return render(request, 'Members/society_expense.html', context)

class Society_Charges(View):
    def get(self,request,**kwargs):
        context ={'society_charges':Charges.objects.all(),'id':request.user.id}
        return render(request, 'Members/society_charges.html', context)

class Payment_History(View):
    def get(self,request,**kwargs):
        payment_details = Income.objects.filter(member=request.user.id)
        print(payment_details)
        context ={'payment_history': payment_details,'id':request.user.id}
        return render(request, 'Members/payment_history.html', context)

class Member_Complaint(View):
    def get(self,request,**kwargs):
        context ={'complaint_details': Complaint.objects.filter(member=request.user.id),'id':request.user.id}
        return render(request, 'Members/complaint_member.html', context)

class Society_Meeting(View):
    def get(self,request,**kwargs):
        context ={'society_meeting':Meeting.objects.all(),'id':request.user.id}
        return render(request, 'Members/society_meeting.html', context)

class Society_Events(View):
    def get(self,request,**kwargs):
        context ={'society_events':Event.objects.all(),'id':request.user.id}
        return render(request, 'Members/society_event.html', context)

class Add_Complaint(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        form = ComplaintCreateForm()
        context = {'id':request.user.id, 'form':form , 'members' : Member.objects.filter(id=request.user.id)}
        return render(request, 'Members/add_complaint.html', context)
    
    def post(self, request, **kwargs):
        form = ComplaintCreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('member_complaint')
        context = {'id':request.user.id, 'form':form}
        return render(request, 'Members/add_complaint.html', context)