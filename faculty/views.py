from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .models import Faculty
from .forms import FacultyForm, FacultyLoginForm
from exams.models import Exam


def faculty_exam_list(request):

    exams = Exam.objects.all().order_by("-exam_date")

    return render(
        request,
        "faculty/exam_list.html",
        {
            "exams": exams,
        }
    )

# ============================================================
# FACULTY LOGIN
# ============================================================

def faculty_login(request):

    if request.user.is_authenticated:

        try:

            request.user.faculty

            return redirect("faculty_dashboard")

        except Faculty.DoesNotExist:

            pass

    if request.method == "POST":

        form = FacultyLoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                try:

                    faculty = user.faculty

                    if not faculty.status:

                        messages.error(
                            request,
                            "Your faculty account is inactive."
                        )

                        return redirect("faculty_login")

                    login(request, user)

                    messages.success(
                        request,
                        f"Welcome, {faculty.first_name}!"
                    )

                    return redirect("faculty_dashboard")

                except Faculty.DoesNotExist:

                    messages.error(
                        request,
                        "This account is not registered as faculty."
                    )

            else:

                messages.error(
                    request,
                    "Invalid username or password."
                )

    else:

        form = FacultyLoginForm()

    return render(
        request,
        "faculty/faculty_login.html",
        {
            "form": form
        }
    )


# ============================================================
# FACULTY REGISTRATION
# ============================================================

def faculty_register(request):

    if request.method == "POST":

        form = FacultyForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(
                username=username,
                email=form.cleaned_data["email"],
                password=password
            )

            faculty = form.save(
                commit=False
            )

            faculty.user = user

            faculty.save()

            messages.success(
                request,
                "Faculty registration completed successfully."
            )

            return redirect("faculty_login")

    else:

        form = FacultyForm()

    return render(
        request,
        "faculty/faculty_register.html",
        {
            "form": form
        }
    )


# ============================================================
# FACULTY DASHBOARD
# ============================================================

def faculty_dashboard(request):

    if not request.user.is_authenticated:

        return redirect("faculty_login")

    try:

        faculty = request.user.faculty

    except Faculty.DoesNotExist:

        messages.error(
            request,
            "Faculty profile not found."
        )

        return redirect("faculty_login")

    # ==============================
    # QUESTION COUNT
    # ==============================

    from questions.models import Question

    question_count = Question.objects.filter(
        subject=faculty.subject
    ).count()

    # ==============================
    # EXAM COUNT
    # ==============================

    from exams.models import Exam

    exam_count = Exam.objects.filter(
        faculty=faculty
    ).count()

    # ==============================
    # STUDENT COUNT
    # ==============================

    from students.models import Student

    student_count = Student.objects.filter(
        department=faculty.department,
        course=faculty.course
    ).count()

    # ==============================
    # SUBJECT COUNT
    # ==============================

    subject_count = 1 if faculty.subject else 0

    # ==============================
    # RECENT EXAMS
    # ==============================

    recent_exams = Exam.objects.filter(
        faculty=faculty
    ).order_by(
        "-exam_date"
    )[:5]

    context = {

        "faculty": faculty,

        "subject_count": subject_count,

        "exam_count": exam_count,

        "question_count": question_count,

        "student_count": student_count,

        "recent_exams": recent_exams,

    }

    return render(
        request,
        "faculty/faculty_dashboard.html",
        context
    )


# ============================================================
# FACULTY PROFILE
# ============================================================

def faculty_profile(request):

    if not request.user.is_authenticated:

        return redirect("faculty_login")

    try:

        faculty = request.user.faculty

    except Faculty.DoesNotExist:

        messages.error(
            request,
            "Faculty profile not found."
        )

        return redirect("faculty_login")

    return render(
        request,
        "faculty/faculty_profile.html",
        {
            "faculty": faculty
        }
    )


# ============================================================
# FACULTY LOGOUT
# ============================================================

from django.contrib.auth import logout
from django.shortcuts import redirect


def faculty_logout(request):

    if request.method == "POST":
        logout(request)
        return redirect("home")

    return redirect("faculty_dashboard")


# ============================================================
# ADMIN FACULTY LIST
# ============================================================

def faculty_list(request):

    faculty_members = Faculty.objects.all().order_by(
        "first_name"
    )

    return render(
        request,
        "faculty/faculty_list.html",
        {
            "faculty_members": faculty_members
        }
    )


# ============================================================
# ADMIN ADD FACULTY
# ============================================================

def faculty_create(request):

    if request.method == "POST":

        form = FacultyForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(
                username=username,
                email=form.cleaned_data["email"],
                password=password
            )

            faculty = form.save(
                commit=False
            )

            faculty.user = user

            faculty.save()

            messages.success(
                request,
                "Faculty added successfully."
            )

            return redirect("faculty_list")

    else:

        form = FacultyForm()

    return render(
        request,
        "faculty/faculty_form.html",
        {
            "form": form,
            "title": "Add Faculty"
        }
    )


# ============================================================
# ADMIN EDIT FACULTY
# ============================================================

def faculty_edit(request, pk):

    faculty = get_object_or_404(
        Faculty,
        pk=pk
    )

    if request.method == "POST":

        form = FacultyForm(
            request.POST,
            instance=faculty
        )

        if form.is_valid():

            form.save()

            if faculty.user:

                faculty.user.email = form.cleaned_data["email"]

                faculty.user.save()

            messages.success(
                request,
                "Faculty updated successfully."
            )

            return redirect("faculty_list")

    else:

        form = FacultyForm(
            instance=faculty
        )

        if faculty.user:

            form.fields["username"].initial = (
                faculty.user.username
            )

    return render(
        request,
        "faculty/faculty_form.html",
        {
            "form": form,
            "title": "Edit Faculty"
        }
    )


# ============================================================
# ADMIN DELETE FACULTY
# ============================================================

def faculty_delete(request, pk):

    faculty = get_object_or_404(
        Faculty,
        pk=pk
    )

    if request.method == "POST":

        if faculty.user:

            faculty.user.delete()

        faculty.delete()

        messages.success(
            request,
            "Faculty deleted successfully."
        )

        return redirect("faculty_list")

    return render(
        request,
        "faculty/faculty_delete.html",
        {
            "faculty": faculty
        }
    )