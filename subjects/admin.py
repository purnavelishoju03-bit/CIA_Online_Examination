from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "course",
        "department",
        "semester",
        "credits",
        "is_active",
    )

    list_filter = (
        "department",
        "course",
        "semester",
    )

    search_fields = (
        "name",
        "code",
    )