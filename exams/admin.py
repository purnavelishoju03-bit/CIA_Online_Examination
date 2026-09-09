from django.contrib import admin
from .models import Exam


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = (
        "exam_name",
        "subject",
        "department",
        "exam_date",
        "status",
    )

    list_filter = (
        "department",
        "course",
        "subject",
        "status",
    )

    search_fields = (
        "exam_name",
        "subject__name",
    )