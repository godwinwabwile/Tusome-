from audioop import reverse
from logging import raiseExceptions
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect 
from userinfo.forms import CreateUserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, "base.html")


def createuser(request):

    global registered
    registered = False

    if request.method == "POST":
        createuserform =CreateUserForm(data=request.POST)
        userprofileform= UserProfileForm(data=request.POST)

        if createuserform.is_valid() and userprofileform.is_valid():
            user=createuserform
            user.save()

            profile= userprofileform.save(commit=False)
            profile.user= user
            profile.save()
            registered= True

        else:
            print(createuserform.errors, userprofileform.errors)
    
    else:
        createuserform=CreateUserForm()
        userprofileform=UserProfileForm()
    return render(request, "userinfo/register.html", {"registered":registered, "createuserform":createuserform, "userprofileform":userprofileform })


def loginuser(request):
    if request.method =="POST":
        username=request.POST.get("username")
        password= request.POST.get("password")

        user=authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("userinfo:index"))
            else:
                return HttpResponse("Account is not active")
        
        else:
            return HttpResponse("invalid Username and Password, please check and try again")

    else:
        return render(request, "userinfo/login.html")

@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse("userinfo:index"))

