from django.urls import path
from . import views

app_name ="carriculum"
urlpatterns= [
    path("", views.StandardListView.as_view(), name="standards_list_view"),
    path("<slug:slug>/", views.SubjectListView.as_view(), name="subject_list"),
    path("<str:standard>/<str:slug>/create/", views.CreateLessonView.as_view(), name="create_lesson"),
    path("<str:standard>/<slug:slug>/", views.LessionsListView.as_view(), name="lessons_list"),
    path("<str:standard>/<str:subject>/<slug:slug>/", views.LessionsDetailView.as_view(), name="lesson_details"),
    path("<str:standard>/<str:subject>/<slug:slug>/update/", views.LessonUpdateView.as_view(), name="lesson_update"),
    
]