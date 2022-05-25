from django.db import models
from django.contrib.auth.models import User
import os


'''method takes an image and renames it'''
def renameprofile(instance, filename):
    upload_to="media/"
    extension=filename.split('.')[-1]

    if instance.user.username:
        filename= "userprofile/{}.{}".format(instance.user.username, extension)       
    return os.path.join(upload_to, filename)



# Create your models here.
class UserProfile(models.Model):
    teacher="teacher"
    student="student"
    applied="applied"
    parent="parent"
    usertypes=[
        (teacher, "teacher"),
        (student, "student"),
        (parent, "parent")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)
    profilepic=models.ImageField(upload_to=renameprofile, blank=True)
    usertype=models.CharField(max_length=20, choices=usertypes, default=student)


    def __str__(self):
        return self.user.username


