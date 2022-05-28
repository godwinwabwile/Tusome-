import os
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.

def renamesubjectavator(instance, filename):
    upload_to="media/"
    extension=filename.split('.')[-1]

    if instance.subject_id:
        filename= "subjects/{}.{}".format(instance.subject_id, extension)       
    return os.path.join(upload_to, filename)

def renamevideo(instance, filename):
    upload_to="media/"
    extension=filename.split('.')[-1]

    if instance.lesson_id:
        filename= "lessons/{}.{}".format(instance.lesson_id, extension)
        if os.path.exists(filename):
            newname= str(instance.lesson_id)+str(1)
            filename= "lessons/{}/{}.{}".format(instance.lesson_id,newname, extension)       
    return os.path.join(upload_to, filename)

def renamepresentation(instance, filename):
    upload_to="media/"
    extension=filename.split('.')[-1]

    if instance.lesson_id:
        filename= "lessons/{}.{}".format(instance.lesson_id, extension)
        if os.path.exists(filename):
            newname= str(instance.lesson_id)+str(1)
            filename= "lessons/{}/{}.{}".format(instance.lesson_id,newname, extension)        
    return os.path.join(upload_to, filename)

def renamenotes(instance, filename):
    upload_to="media/"
    extension=filename.split('.')[-1]

    if instance.lesson_id:
        filename= "lessons/{}.{}".format(instance.lesson_id, extension)
        if os.path.exists(filename):
            newname= str(instance.lesson_id)+str(1)
            filename= "lessons/{}/{}.{}".format(instance.lesson_id,newname, extension)        
    return os.path.join(upload_to, filename)


class Standard(models.Model):
    name= models.CharField(max_length=50)
    description= models.TextField(max_length=500, blank=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super().save(*args, **kwargs)
    

class Subject(models.Model):
    subject_id= models.CharField(max_length=20, unique=True)
    name= models.CharField(max_length=50)
    description= models.TextField(max_length=500, blank=True)
    standard=models.ForeignKey(Standard, on_delete=models.CASCADE, related_name="subjects")
    avator= models.ImageField(upload_to=renamesubjectavator, blank=True, verbose_name="Subject Avator")
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        std = self.subject_id[:4]
        delim= "_"
        object= std+delim+self.name
        return object

    
    def save(self, *args, **kwargs):
        self.slug= slugify(self.subject_id)
        super().save(*args, **kwargs)
    
    
    
class Lesson(models.Model):
    lesson_id=models.CharField(max_length=25, unique=True)
    name=models.CharField(max_length=30)
    position=models.PositiveSmallIntegerField(verbose_name="Chapter Number:")
    video = models.FileField(upload_to=renamevideo, blank=True, null=True, verbose_name="Lesson Video")
    presentation= models.FileField(upload_to=renamepresentation, blank=True, null=True, verbose_name="Lesson presentationj")
    notes= models.FileField(upload_to=renamenotes, blank=True, null=True, verbose_name="Lesson Notes")
    
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="lessons")
    slug= models.SlugField(null=True, blank=True)

    class Meta:
        ordering= ['position']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("carriculum:lessons_list", kwargs={"standard":self.subject.standard.slug, "slug":self.subject.slug})

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super().save(*args, *kwargs)

    
class Discussion(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_name= models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="discussion")
    post_name=models.CharField(max_length=145)
    body=models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.post_name = slugify("Post by"+ "-"+ str(self.author) + str(self.created_date))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.post_name

    class Meta:
        ordering =['created_date']

class Reply(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    post_name=models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="replies")
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        returnstring = "reply to" + str(self.post_name.post_name)
        return returnstring

    



