from django.db import models
from departments.models import Department
from courses.models import Course


class Subject(models.Model):

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    name = models.CharField(max_length=150)

    code = models.CharField(
        max_length=20,
        unique=True
    )

    semester = models.PositiveIntegerField()

    credits = models.PositiveIntegerField(default=4)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "subjects"
        ordering = ["semester", "name"]

    def __str__(self):
        return self.name