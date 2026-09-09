from django.db import models
from departments.models import Department
from courses.models import Course
from subjects.models import Subject
from faculty.models import Faculty


class Exam(models.Model):
    STATUS_CHOICES = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    )

    exam_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    total_marks = models.PositiveIntegerField(default=30)
    pass_marks = models.PositiveIntegerField(default=12)

    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    duration = models.PositiveIntegerField(help_text="Duration in Minutes")

    instructions = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-exam_date"]

    def __str__(self):
        return self.exam_name