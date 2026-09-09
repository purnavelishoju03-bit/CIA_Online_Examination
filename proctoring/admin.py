from django.contrib import admin

from .models import ProctoringEvent


@admin.register(ProctoringEvent)
class ProctoringEventAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "exam",
        "event_type",
        "severity",
        "created_at",
    )

    list_filter = (
        "event_type",
        "severity",
        "exam",
    )

    search_fields = (
        "student__roll_number",
        "student__first_name",
        "student__last_name",
        "exam__exam_name",
    )

    ordering = (
        "-created_at",
    )