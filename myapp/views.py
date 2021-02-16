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
                     return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request,'myapp/login.html',{'form':fm,})
    else:
        messages.info(request,'logout in order to login with different aaccount.')
        return HttpResponseRedirect('/dashboard/')

def dashboard(request):
    if request.user.is_authenticated:
        posts=StudentModel.objects.all()
        user = request.user
        fname = user.get_full_name()
       
        return render(request,'myapp/dashboard.html',{
            'posts':posts,
            'name':user,
            'fname':fname,
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
                messages.success(request,'Post Published Successfuly')
                fm = QuerryForm()
        else:
            fm = QuerryForm()
      
        return render(request,'myapp/querry.html',{
            'form':fm,
            })
    else:
        return HttpResponseRedirect('/login/')
def edit_query(request,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = StudentModel.objects.get(pk=id)
            fm = QuerryForm(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
        else:
            pi = StudentModel.objects.get(pk=id)
            fm = QuerryForm(instance=pi)
        return render(request,'myapp/update.html',{'form':fm})
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
