from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MyChangeFormPassword, MemberEditForm
from .models import Member
import json
from django.contrib.auth import update_session_auth_hash

class Profile(LoginRequiredMixin,View):
    def get(self,request): 
        members = Member.objects.get(id=request.user.id)
        context = {'member':members}
        return render(request, 'Members/profile.html',context)  

class Edit_Profile(LoginRequiredMixin,View):
    def get(self,request,**kwargs): 
        members = Member.objects.get(id=kwargs['id'])
        context = {'member':members,'id':kwargs['id']}
        return render(request, 'Members/profile.html',context)  


    def post(self, request):
        post_data =  json.loads(request.body.decode("utf-8"))
        member = Member.objects.get(id = request.user.id)
        form = MemberEditForm(post_data, instance=member)
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
