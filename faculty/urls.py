from django.urls import path
from . import views

urlpatterns = [

    # ========================================================
    # FACULTY LOGIN
    # ========================================================

    path(
        "login/",
        views.faculty_login,
        name="faculty_login"
    ),


    # ========================================================
    # FACULTY REGISTRATION
    # ========================================================

    path(
        "register/",
        views.faculty_register,
        name="faculty_register"
    ),


    # ========================================================
    # FACULTY DASHBOARD
    # ========================================================

    path(
        "dashboard/",
        views.faculty_dashboard,
        name="faculty_dashboard"
    ),


    # ========================================================
    # FACULTY PROFILE
    # ========================================================

    path(
        "profile/",
        views.faculty_profile,
        name="faculty_profile"
    ),


    # ========================================================
    # FACULTY LOGOUT
    # ========================================================

    path(
        "logout/",
        views.faculty_logout,
        name="faculty_logout"
    ),


    # ========================================================
    # FACULTY EXAMINATIONS
    # ========================================================

    path(
        "exams/",
        views.faculty_exam_list,
        name="faculty_exam_list"
    ),


    # ========================================================
    # FACULTY MANAGEMENT
    # ========================================================

    path(
        "list/",
        views.faculty_list,
        name="faculty_list"
    ),

    path(
        "create/",
        views.faculty_create,
        name="faculty_create"
    ),

    path(
        "edit/<int:pk>/",
        views.faculty_edit,
        name="faculty_edit"
    ),

    path(
        "delete/<int:pk>/",
        views.faculty_delete,
        name="faculty_delete"
    ),

]