from django.contrib import admin
from .models import Faculty

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "department",
        "course",
        "subject",
        "designation",
        "status",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
    )

    list_filter = (
        "department",
        "course",
        "subject",
        "status",
    )