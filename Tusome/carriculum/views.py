from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import LessonForm
from django.views.generic import FormView, TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Standard, Lesson, Subject 

# Create your views here.

class CreateLessonView(CreateView):
     form_class = LessonForm
     context_object_name = "subject"
     model= Subject
     template_name = "carriculum/createlesson.html"


     def get_success_url(self):
          self.object =self.get_object()
          standard=self.object.standard
          return reverse_lazy("carriculum:lessons_list", kwargs={"standard":standard,"slug":self.object.slug})
     
     def form_valid(self, form, *args, **kwargs):
          self.object = self.get_object()
          fm =form.save(commit=False)
          fm.created_by=self.request.user
          fm.standard = self.object.standard
          fm.subject= self.object
          fm.save()
          return HttpResponseRedirect(self.get_success_url())

class LessonUpdateView(UpdateView):
     context_object_name="lessons"
     model= Lesson
     fields = ("name", "position", "video", "presentation", "notes")
     templaten_name= "carriculum/lesson_form.html"

     
          
class StandardListView(ListView):
     context_object_name= "standards"
     model = Standard
     template_name= "carriculum/standard_list_view.html"

class SubjectListView(DetailView):
     context_object_name= "standard"
     model = Standard
     template_name= "carriculum/subject_list_view.html"

class LessionsListView(DetailView):
     context_object_name= "lessons"
     model = Subject
     template_name= "carriculum/lessons_list_view.html"

class LessionsDetailView(DetailView):
     context_object_name= "lessons"
     model = Lesson
     template_name= "carriculum/lessons_detail_view.html"


