from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View,TemplateView,ListView,CreateView,DetailView
from students.forms import StudentDetailForm
from students.models import Student
from django.urls import reverse_lazy


class Home(TemplateView):
    template_name = "home.html"

class AddStudentView(CreateView):
    form_class = StudentDetailForm
    template_name = "add_student.html"
    success_url =reverse_lazy('home')


class StudentsDetailView(ListView):
    model = Student
    context_object_name = "Students"
    template_name = "studentsdetails.html"



class StudentDetailView(DetailView):
    model = Student
    context_object_name = "Student"
    template_name = "studentdetails.html"
    pk_url_kwarg = "pk"


def add_marks(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        marks = request.POST.get('marks')
        student.marks = marks
        student.save()
        return redirect('studentdetails', pk=pk)  # Redirect to student detail view after adding marks

    return render(request, 'add_marks.html', {'student': student})


def student_mark(request, pk):
    student = get_object_or_404(Student, pk=pk)
    mark = student.marks
    return render(request, 'student_mark.html', {'student': student, 'mark': mark})


def student_result(request):
    students=Student.objects.all()

    student_grade=[]
    for student in students:
        mark=student.marks
        if mark is None:
            grade = 'N/A'
        elif 91 <= mark <= 100:
            grade="S"
        elif 81 <= mark <= 90:
            grade = 'A'
        elif 71<=mark<=80:
            grade='B'
        elif 61 <= mark <= 70:
            grade = 'C'
        elif 51 <= mark <= 60:
            grade = 'D'
        elif 41 <= mark <= 50:
            grade = 'B'

        else:
            grade='F'

        student_grade.append({'student': student, 'grade': grade})
    return render(request, 'student_list.html', {'student_grades': student_grade})














