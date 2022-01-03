from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login;
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import MemberEditForm
from .models import Member

class Profile(LoginRequiredMixin,View):
    def get(self,request,**kwargs): 
        members = Member.objects.get(id=kwargs['id'])
        context = {'member':members,'id':kwargs['id']}
        return render(request, 'Members/profile.html',context)  

class Edit_Profile(LoginRequiredMixin,View):
    def get(self,request,**kwargs): 
        members = Member.objects.get(id=kwargs['id'])
        form = MemberEditForm(instance=members)
        context = {'member':members,'id':kwargs['id'], 'form':form}
        return render(request, 'Members/edit_profile.html',context)  

    def post(self, request, **kwargs):
        # members = Member.objects.get(id=kwargs['id'])
        member = get_object_or_404(Member, id=kwargs['id'])
        form = MemberEditForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return redirect('profile', id=kwargs['id'])
        else:
            print(form.errors)
        
        context = {'form':form,'member':member}
        return render(request, 'Members/edit_profile.html', context)    
