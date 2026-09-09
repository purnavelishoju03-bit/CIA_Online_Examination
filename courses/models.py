from django.db import models
from departments.models import Department


class Course(models.Model):

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=150)

    code = models.CharField(
        max_length=20,
        unique=True
    )

    duration = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.name