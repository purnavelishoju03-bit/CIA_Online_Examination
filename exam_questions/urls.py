from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.exam_question_list,
        name="exam_question_list"
    ),

    path(
        "mapping/",
        views.exam_question_mapping,
        name="exam_question_mapping"
    ),

    path(
        "add/",
        views.exam_question_add,
        name="exam_question_add"
    ),

    path(
        "edit/<int:id>/",
        views.exam_question_edit,
        name="exam_question_edit"
    ),

    path(
        "delete/<int:id>/",
        views.exam_question_delete,
        name="exam_question_delete"
    ),
]