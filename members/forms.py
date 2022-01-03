from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Member
from .managers import CustomUserManager
import string
import random
from django.forms import ModelForm

def generate_pwd():
    s1 = list(string.ascii_uppercase);
    s2 = list(string.ascii_lowercase);
    s3 = list(string.digits);
    s = [];
    s.extend(s1);
    s.extend(s2);
    s.extend(s3);
    random.shuffle(s);
    return("".join(s[0:10]))


class CustomUserCreationForm(UserCreationForm, CustomUserManager):
    password1 = None
    password2 = None
    def clean(self, **extra_fields):
        password = generate_pwd()
        # Set passowrd  
        print(password)
        self.cleaned_data['password1'] = password
        self.cleaned_data['password2'] = password

        # Sending a long credentials to the resident user
        print(self.cleaned_data)
        subject = "Smart Society System"
        from_email = settings.EMAIL_HOST_USER
        to_email =  self.cleaned_data['email']
        html_content = render_to_string('Members/email_template.html', {'first_name': self.cleaned_data['first_name'],'last_name': self.cleaned_data['last_name'],'username':self.cleaned_data['flat_Number'], 'password': self.cleaned_data['password1']})
        text_content = strip_tags(html_content)
        # send_mail(subject, text_content, from_email, [to_email], fail_silently=False)

        return super().clean()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["flat_Number"]
        user.set_password(self.cleaned_data["password1"])
        print(self.cleaned_data['flat_Type'])
        if self.cleaned_data['flat_Type'] == "1rk":
            user.area = 300
        else:
            user.area = 600
        return user

class MemberEditForm(ModelForm):
    class Meta:
        model = Member
        fields = ['first_name','last_name','phone_Number','wing','floor_Number','flat_Number','flat_Type','area']