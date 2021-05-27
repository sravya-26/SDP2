from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


# from .models import Customer

# Create your forms here.

class ContactForm(forms.Form):
    Enter_Name = forms.CharField(required=True,label=mark_safe(' <br /><br />Enter Name'))
    Enter_Email = forms.EmailField(required=True, label=mark_safe(' <br /><br />Enter Email'))
    Message = forms.CharField(
        required=True,
        widget=forms.Textarea, 
        label=mark_safe(' <br /><br /> Message')
    )


# class CreateUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password1', 'password2']
