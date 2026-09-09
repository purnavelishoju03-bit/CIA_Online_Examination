from django.db import models
from students.models import Student
from exams.models import Exam


class Result(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )

    obtained_marks = models.PositiveIntegerField(default=0)

    total_marks = models.PositiveIntegerField()

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=10,
        choices=(
            ("Pass", "Pass"),
            ("Fail", "Fail"),
        )
    )

    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "exam")

    def __str__(self):
        return f"{self.student.roll_number} - {self.exam.exam_name}"