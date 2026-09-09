from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.question_list,
        name="question_list"
    ),

    path(
        "load-subjects/",
        views.load_subjects,
        name="load_subjects"
    ),

    path(
        "upload/",
        views.question_upload_excel,
        name="question_upload_excel"
    ),

    path(
        "view/<int:id>/",
        views.question_view,
        name="question_view"
    ),

    path(
        "delete/<int:id>/",
        views.question_delete,
        name="question_delete"
    ),

]