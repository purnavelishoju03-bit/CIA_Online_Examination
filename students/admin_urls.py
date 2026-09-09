
from django.urls import path

from . import views


urlpatterns = [

    # ==========================================================
    # STUDENT MANAGEMENT
    # ==========================================================

    # Student List
    # /admin-panel/students/

    path(
        "",
        views.student_list,
        name="student_list"
    ),

    # Create Student
    # /admin-panel/students/create/

    path(
        "create/",
        views.student_create,
        name="student_create"
    ),

    # Edit Student
    # /admin-panel/students/1/edit/

    path(
        "<int:pk>/edit/",
        views.student_edit,
        name="student_edit"
    ),

    # Delete Student
    # /admin-panel/students/1/delete/

    path(
        "<int:pk>/delete/",
        views.student_delete,
        name="student_delete"
    ),

    # Bulk Upload Students
    # /admin-panel/students/bulk-upload/

    path(
        "bulk-upload/",
        views.student_bulk_upload,
        name="student_bulk_upload"
    ),

    # Upload Success
    # /admin-panel/students/upload-success/

    path(
        "upload-success/",
        views.student_upload_success,
        name="student_upload_success"
    ),

    # Download Student Credentials
    # /admin-panel/students/download-credentials/

    path(
        "download-credentials/",
        views.download_student_credentials,
        name="download_student_credentials"
    ),
]

