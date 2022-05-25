from cProfile import label
from django import forms
from django.contrib.auth.models import User
from userinfo.models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta():
        model = User
        fields= ("username","first_name", "last_name", "email", "password", "password2")

        label={
            'password':'Password',
            'password2':'Confirm Password'
        }

class UserProfileForm(forms.ModelForm):
    bio= forms.CharField(required=False)
    teacher="teacher"
    student="student"
    apply="applied"
    parent="parent"
    usertypes=[
        (student, "student"),
        (parent, "parent"),
        (apply, "applied")
    ]
    usertype= forms.ChoiceField(required=True, choices=usertypes)

    class Meta():
        model= UserProfile

        fields =("bio", "usertype", "profilepic")