from django.urls import path
from students import views
from .views import add_marks,student_mark,student_result

urlpatterns = [
path('home',views.Home.as_view(),name="home"),
path('add/',views.AddStudentView.as_view(),name="add_details"),
path('students/',views.StudentsDetailView.as_view(),name='studentsdetails'),
path('student/details/<int:pk>',views.StudentDetailView.as_view(),name='studentdetails'),
path('students/<int:pk>/add_marks/',add_marks, name='add_marks'),
path('students/<int:pk>/mark/', student_mark, name='student_mark'),
path('students/result/', student_result, name='student_list'),
]