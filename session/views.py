from email import message
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm,UserProfileForm
from .models import UserProfile


from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def loginuser(request):
    if request.method=="POST" :
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid:
            # username=form.cleaned_data.get('username')
            # password=form.cleaned_data.get('password')
            username=request.POST['username']
            password=request.POST['password']
         
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("homeview")
            else:
                messages.error(request,"Invalid username or password!")
        else:
            messages.error(request,"Invalid username or password!")
    else:
        form=AuthenticationForm()
    return render(request,'session/login.html',{'form':form})

def logoutuser(request):
    logout(request)
    messages.success(request,"Successfully logout!")
    return redirect("homeview")

def register(request):
    if request.method=="POST":
        form =SignUpForm(request.POST)
        if form.is_valid:
            user=form.save()
            current_site=get_current_site(request)
            mail_subject='An Account Created'
            message =render_to_string('session/account.html',{
                'user':user,
                'domain': current_site.domain
            })
            send_mail=form.cleaned_data.get('email')
            email =EmailMessage(mail_subject,message,to=[send_mail])
            email.send()
            messages.success(request,'Successfuly created account')
            return redirect('session:login')
    else:
        form =SignUpForm()
    return render(request,'session/signup.html',{'form':form})

def changepass(request):
    if request.method=="POST":
        form =PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid:
            u = User.objects.get(username__exact=form.user)
            u.set_password(request.POST['new_password1'])
            u.save()
            update_session_auth_hash(request, u)
           
            # update_session_auth_hash(request,form.user)
            messages.success(request,"Successfully password changed!")
            return redirect("homeview")
    else:
        form =PasswordChangeForm(user=request.user)
    return render(request,'session/change.html',{'form':form})

def UserProfile(request):
    try:
        instance=UserProfile.objects.get(user=request.user)
    except :
        instance=None
    if request.method=="POST":
        if instance:
            form=UserProfileForm(request.POST,request.FILES,instance=instance)
        else:
            form=UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request,"success saved")
            return redirect("homeview")
    else: 
        form=UserProfileForm(instance=instance)
    context={
        'form':form
    }
    return render(request,'session/userproCreate.html',context)

def ownprofile(request):
    user=request.user
    return render(request,'session/userprofile.html',{'user':user})
