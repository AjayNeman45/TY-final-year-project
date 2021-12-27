from django.contrib import admin
from django.contrib.admin.decorators import display
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from .models import CommiteeMember, Member

class MembersAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = Member
    list_display = ('first_name','last_name','phone_Number','email','wing', 'floor_Number','flat_Number','flat_Type','area','member_Type','username')
    list_filter = ()
    fieldsets = (
        ('Persomal Info', {'fields': ('username', 'email', 'password','first_name','last_name','phone_Number', 'profile_Photo')}),
        ('Address', {'fields': ('wing','floor_Number','flat_Number')}),
        ('Flat Info', {'fields' : ('flat_Type', 'area','member_Type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email', 'phone_Number','profile_Photo',
                 'wing','floor_Number', 'flat_Number',
                 'flat_Type','member_Type',
                 'is_active','is_staff')}
        ),
    )
    ordering = ('id',)


admin.site.register(Member, MembersAdmin)

class CommiteeMemberAdmin(admin.ModelAdmin):
    list_display = ("get_member_name","position","from_Date")
    @display(ordering='Complaint__first_Name', description="member")
    def get_member_name(self,obj):
        return obj.member.first_name +  " " + obj.member.last_name

admin.site.register(CommiteeMember, CommiteeMemberAdmin)

admin.site.unregister(Group)