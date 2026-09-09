from django.shortcuts import render
from departments.models import Department
from courses.models import Course
from subjects.models import Subject
from faculty.models import Faculty
from students.models import Student

def dashboard(request):

    total_departments = Department.objects.count()

    total_courses = Course.objects.count()

    total_subjects = Subject.objects.count()


    context = {
        "total_departments": Department.objects.count(),
        "total_courses": Course.objects.count(),
        "total_subjects": Subject.objects.count(),
        "total_faculty": Faculty.objects.count(),
        "total_students": 0,
        "active_exams": 0,
    }

    return render(
        request,
        "admin_panel/dashboard.html",
        context
    )

    
def departments(request):
    return render(request, "admin_panel/departments/index.html")

def courses(request):
    return render(request, "admin_panel/courses/index.html")

def subjects(request):
    return render(request, "admin_panel/subjects/index.html")

def faculty(request):
    return render(request, "admin_panel/faculty/index.html")

def exams(request):
    return render(request, "admin_panel/exams/index.html")

def add_exam(request):
    return render(request, "admin_panel/exams/create.html")

def assign_exam(request):
    return render(request, "admin_panel/exams/assign.html")

def question_bank(request):
    return render(request, "admin_panel/question_bank/index.html")

def add_question(request):
    return render(request, "admin_panel/question_bank/create.html")

def reports(request):
    return render(request, "admin_panel/reports/index.html")