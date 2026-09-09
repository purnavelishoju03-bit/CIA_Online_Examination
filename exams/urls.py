from django.urls import path
from . import views


urlpatterns = [

    # Exam List
    path('', views.exam_list, name='exam_list'),


    # Create Exam
    path('add/', views.exam_create, name='exam_create'),


    # Edit Exam
    path('edit/<int:pk>/', views.exam_edit, name='exam_edit'),


    # Delete Exam
    path('delete/<int:pk>/', views.exam_delete, name='exam_delete'),

]