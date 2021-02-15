from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import StudentModel
from django import forms

class StudentRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        labels = {
            'username':'Enter Username',
            'email':'Enter Email',
        }


class QuerryForm(forms.ModelForm):

    class Meta:
        model = StudentModel
        fields = ['title','querry',]
        labels = {
            'title':'ENTER POST TITLE',
          
            'querry':'WRITE POST',
        }
       
        
class StudentProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined',]

class AdminProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'