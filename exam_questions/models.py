from django.db import models

from exams.models import Exam
from questions.models import Question


class ExamQuestion(models.Model):

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="exam_questions"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="mapped_exams"
    )

    question_order = models.PositiveIntegerField(
        default=1
    )

    class Meta:

        ordering = ["question_order"]

        constraints = [
            models.UniqueConstraint(
                fields=["exam", "question"],
                name="unique_exam_question"
            )
        ]

    def __str__(self):

        return (
            f"{self.exam.exam_name} - "
            f"Question {self.question_order}"
        )