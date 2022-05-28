
from django import forms
from carriculum.models import Lesson, Subject, Standard


class LessonForm(forms.ModelForm):
    
    class Meta():
        model=Lesson
        fields= ("lesson_id", "position","name", "video", "presentation", "notes" )