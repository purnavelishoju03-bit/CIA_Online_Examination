from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from accounts import views as account_views
from students import views as student_views

from django.contrib.auth import views as auth_views


urlpatterns = [

    # ============================================================
    # HOME
    # ============================================================

    path(
        "",
        account_views.home,
        name="home"
    ),


    # ============================================================
    # STUDENT LOGIN
    # ============================================================

    # URL:
    # http://127.0.0.1:8000/student-login/

    path(
        "student-login/",
        student_views.student_login,
        name="student_login"
    ),


    # ============================================================
    # STUDENT PORTAL
    # ============================================================

    # URLs:
    #
    # /students/login/
    # /students/dashboard/
    # /students/exams/
    # /students/exam/<id>/readiness/
    # /students/exam/<id>/start/
    # /students/results/
    # /students/profile/
    # /students/logout/

    path(
        "students/",
        include("students.urls")
    ),


    # ============================================================
    # ADMIN LOGIN
    # ============================================================

    path(
        "admin-login/",
        account_views.admin_login,
        name="admin_login"
    ),


    # ============================================================
    # DJANGO ADMIN
    # ============================================================

    path(
        "admin/",
        admin.site.urls
    ),


    # ============================================================
    # ADMIN PANEL
    # ============================================================

    path(
        "admin-panel/",
        include("admin_panel.urls")
    ),


    # ============================================================
    # DEPARTMENTS
    # ============================================================

    path(
        "admin-panel/departments/",
        include("departments.urls")
    ),


    # ============================================================
    # COURSES
    # ============================================================

    path(
        "admin-panel/courses/",
        include("courses.urls")
    ),


    # ============================================================
    # SUBJECTS
    # ============================================================

    path(
        "admin-panel/subjects/",
        include("subjects.urls")
    ),


    # ============================================================
    # FACULTY MANAGEMENT
    # ============================================================

    path(
        "admin-panel/faculty/",
        include("faculty.urls")
    ),


    # ============================================================
    # STUDENT MANAGEMENT
    # ============================================================

    path(
        "admin-panel/students/",
        include("students.admin_urls")
    ),


    # ============================================================
    # EXAMS
    # ============================================================

    path(
        "admin-panel/exams/",
        include("exams.urls")
    ),


    # ============================================================
    # QUESTIONS
    # ============================================================

    path(
        "admin-panel/questions/",
        include("questions.urls")
    ),


    # ============================================================
    # EXAM QUESTIONS
    # ============================================================

    path(
        "admin-panel/exam-questions/",
        include("exam_questions.urls")
    ),


    # ============================================================
    # RESULTS
    # ============================================================

    path(
        "admin-panel/results/",
        include("results.urls")
    ),


    # ============================================================
    # FACULTY PORTAL
    # ============================================================

    path(
        "faculty/",
        include("faculty.urls")
    ),


    # ============================================================
    # PROCTORING
    # ============================================================

    path(
        "proctoring/",
        include("proctoring.urls")
    ),


    # ============================================================
    # GLOBAL LOGOUT
    # ============================================================

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),
]


# ================================================================
# MEDIA
# ================================================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )