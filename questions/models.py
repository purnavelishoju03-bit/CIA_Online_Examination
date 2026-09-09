from django.db import models
from subjects.models import Subject


class Question(models.Model):

    # ==========================================================
    # DIFFICULTY
    # ==========================================================

    DIFFICULTY_CHOICES = (
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    )


    # ==========================================================
    # STATUS
    # ==========================================================

    STATUS_CHOICES = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    )


    # ==========================================================
    # QUESTION TYPE
    # ==========================================================

    QUESTION_TYPE_CHOICES = (
        ("MCQ", "Multiple Choice"),
        ("IMAGE", "Image Question"),
        ("VOICE", "Voice Question"),
    )


    # ==========================================================
    # SUBJECT
    # ==========================================================

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )


    # ==========================================================
    # QUESTION TYPE
    # ==========================================================

    question_type = models.CharField(
        max_length=10,
        choices=QUESTION_TYPE_CHOICES,
        default="MCQ"
    )


    # ==========================================================
    # QUESTION TEXT
    # ==========================================================

    question = models.TextField(
        blank=True,
        null=True
    )


    # ==========================================================
    # QUESTION IMAGE
    # ==========================================================

    question_image = models.ImageField(
        upload_to="questions/",
        blank=True,
        null=True
    )


    # ==========================================================
    # OPTIONS
    # ==========================================================

    option_a = models.CharField(
        max_length=255
    )

    option_b = models.CharField(
        max_length=255
    )

    option_c = models.CharField(
        max_length=255
    )

    option_d = models.CharField(
        max_length=255
    )


    # ==========================================================
    # CORRECT ANSWER
    # ==========================================================

    correct_answer = models.CharField(
        max_length=1,
        choices=(
            ("A", "Option A"),
            ("B", "Option B"),
            ("C", "Option C"),
            ("D", "Option D"),
        )
    )


    # ==========================================================
    # MARKS
    # ==========================================================

    marks = models.PositiveIntegerField(
        default=1
    )


    # ==========================================================
    # DIFFICULTY
    # ==========================================================

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default="Easy"
    )


    # ==========================================================
    # STATUS
    # ==========================================================

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Active"
    )


    # ==========================================================
    # CREATED DATE
    # ==========================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    # ==========================================================
    # META
    # ==========================================================

    class Meta:

        ordering = [
            "subject",
            "id"
        ]


    # ==========================================================
    # STRING
    # ==========================================================

    def __str__(self):

        if self.question_type == "IMAGE":

            return f"Image Question - {self.id}"

        if self.question:

            return self.question[:60]

        return f"Question - {self.id}"