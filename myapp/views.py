from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import StudentRegistrationForm, QuerryForm, StudentProfileForm, AdminProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import StudentModel
# Create your views here.

#home page
def index(request):
    stud = StudentModel.objects.all()
    return render(request,'myapp/index.html',{'queries':stud,})
#Student Registration Form
def StudentRegistration(request):
    if request.method == 'POST':
        fm = StudentRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Student Registered Successfully!!!')
    else:
        fm = StudentRegistrationForm()
    
    return render(request,'myapp/registration.html',{'form':fm,})

#Student Login Form
def StudentLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data = request.POST)
            if fm.is_valid():
                 uname = fm.cleaned_data['username']
                 upass = fm.cleaned_data['password']
                 user = authenticate(username=uname, password = upass)
                 if user is not None:
                     login(request,user)
                     messages.success(request,'Logged in successfully !!')
                     return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'myapp/login.html',{'form':fm,})
    else:
        messages.info(request,'logout in order to login with different aaccount.')
        return HttpResponseRedirect('/profile/')
        
def StudentProfile(request):
    if request.user.is_authenticated:
        if request.method =='POST':
           if request.user.is_superuser == True:
               fm = AdminProfileForm(request.POST, instance=request.user)
           else:
               fm = StudentProfileForm(request.POST, instance=request.user)
        
           if fm.is_valid():
               messages.success(request,'Successfully updated') 
        else:
            if request.user.is_superuser == True:
                fm = AdminProfileForm(instance=request.user)
            else:
                fm = StudentProfileForm(instance=request.user)
        return render(request,'myapp/profile.html',{
            'name':request.user,
            'form':fm,
        })
    else:
        return HttpResponseRedirect('/login/')


#logout

def StudentLogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def StudentQuerry(request):
    if request.user.is_authenticated:
        if request.method =='POST':
             fm = QuerryForm(request.POST)
             if fm.is_valid():
                fm.save()
                messages.success(request,'Your Querry has sent successfuly')
                fm = QuerryForm()
        else:
            fm = QuerryForm()
      
        return render(request,'myapp/querry.html',{
            'form':fm,
            })
    else:
        return HttpResponseRedirect('/login/')

def delete_Query(request,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = StudentModel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/')
    else:
        messages.info(request,'Login First')
        return HttpResponseRedirect('/login/')
