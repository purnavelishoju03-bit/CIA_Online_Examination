from django.urls import path

from . import views


urlpatterns = [

    # ==========================================================
    # STUDENT DASHBOARD
    # URL: /students/dashboard/
    # ==========================================================

    path(
        "dashboard/",
        views.student_dashboard,
        name="student_dashboard"
    ),

    # ==========================================================
    # AVAILABLE EXAMS
    # URL: /students/exams/
    # ==========================================================

    path(
        "exams/",
        views.student_exam_list,
        name="student_exam_list"
    ),

    # ==========================================================
    # EXAM READINESS CHECK
    # URL: /students/exam/6/readiness/
    # ==========================================================

    path(
        "exam/<int:exam_id>/readiness/",
        views.student_exam_readiness,
        name="student_exam_readiness"
    ),

    # ==========================================================
    # ACTUAL EXAM
    # URL: /students/exam/6/start/
    # ==========================================================

    path(
        "exam/<int:exam_id>/start/",
        views.student_start_exam,
        name="student_start_exam"
    ),

    # ==========================================================
    # STUDENT RESULTS
    # URL: /students/results/
    # ==========================================================

    path(
        "results/",
        views.student_results,
        name="student_results"
    ),

    # ==========================================================
    # STUDENT PROFILE
    # URL: /students/profile/
    # ==========================================================

    path(
        "profile/",
        views.student_profile,
        name="student_profile"
    ),

    # ==========================================================
    # STUDENT LOGOUT
    # URL: /students/logout/
    # ==========================================================

    path(
        "logout/",
        views.student_logout,
        name="student_logout"
    ),
]