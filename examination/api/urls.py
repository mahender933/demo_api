from django.urls import path
from . import views

app_name = "exam"
urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('exam-list/', views.exams_list, name='exams_list'),
    path('subject-list/', views.subject_list, name='subject_list'),
    path('add-exam/', views.add_exam, name='add_exam'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-subject/', views.add_subject, name='add_subject'),
    path('add-topic/', views.add_topic, name='add_topic'),
    path('show-hierarchy/<int:exam_id>/', views.show_hierarchy, name='show_hierarchy'),
]

