
from django.shortcuts import render

from departments.models import Department
from courses.models import Course
from subjects.models import Subject
from faculty.models import Faculty
from students.models import Student
from exams.models import Exam
from questions.models import Question


def dashboard(request):

    # =========================================================
    # DASHBOARD COUNTS
    # =========================================================

    department_count = Department.objects.count()

    course_count = Course.objects.count()

    subject_count = Subject.objects.count()

    faculty_count = Faculty.objects.count()

    student_count = Student.objects.count()

    exam_count = Exam.objects.filter(status="Active").count()

    question_count = Question.objects.count()


    # =========================================================
    # DASHBOARD CONTEXT
    # =========================================================

    context = {

        "department_count": department_count,

        "course_count": course_count,

        "subject_count": subject_count,

        "faculty_count": faculty_count,

        "student_count": student_count,

        "exam_count": exam_count,

        "question_count": question_count,

    }


    return render(
        request,
        "admin_panel/dashboard.html",
        context
    )


# =============================================================
# OTHER ADMIN PAGES
# =============================================================

def departments(request):
    return render(
        request,
        "admin_panel/departments/index.html"
    )


def courses(request):
    return render(
        request,
        "admin_panel/courses/index.html"
    )


def subjects(request):
    return render(
        request,
        "admin_panel/subjects/index.html"
    )


def faculty(request):
    return render(
        request,
        "admin_panel/faculty/index.html"
    )


def exams(request):
    return render(
        request,
        "admin_panel/exams/index.html"
    )


def add_exam(request):
    return render(
        request,
        "admin_panel/exams/create.html"
    )


def assign_exam(request):
    return render(
        request,
        "admin_panel/exams/assign.html"
    )


def question_bank(request):
    return render(
        request,
        "admin_panel/question_bank/index.html"
    )


def add_question(request):
    return render(
        request,
        "admin_panel/question_bank/create.html"
    )


def reports(request):
    return render(
        request,
        "admin_panel/reports/index.html"
    )

