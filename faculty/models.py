from django.db import models
from django.contrib.auth.models import User

from departments.models import Department
from courses.models import Course
from subjects.models import Subject


class Faculty(models.Model):

    # ==============================
    # FACULTY BASIC INFORMATION
    # ==============================

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=15
    )

    # ==============================
    # ACADEMIC INFORMATION
    # ==============================

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    # ==============================
    # LOGIN USER
    # ==============================

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="faculty"
    )

    # ==============================
    # PROFESSIONAL INFORMATION
    # ==============================

    designation = models.CharField(
        max_length=100
    )

    qualification = models.CharField(
        max_length=100
    )

    experience = models.PositiveIntegerField(
        default=0
    )

    # ==============================
    # STATUS
    # ==============================

    status = models.BooleanField(
        default=True
    )

    # ==============================
    # CREATED DATE
    # ==============================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # ==============================
    # DISPLAY NAME
    # ==============================

    def __str__(self):
        return f"{self.first_name} {self.last_name}"