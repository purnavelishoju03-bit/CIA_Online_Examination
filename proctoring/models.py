from django.db import models

# Create your models here.
from django.db import models

from students.models import Student
from exams.models import Exam


class ProctoringEvent(models.Model):

    EVENT_TYPES = (
        ("CAMERA_STARTED", "Camera Started"),
        ("CAMERA_STOPPED", "Camera Stopped"),
        ("MIC_STARTED", "Microphone Started"),
        ("MIC_STOPPED", "Microphone Stopped"),
        ("TAB_SWITCH", "Tab Switch"),
        ("FULLSCREEN_EXIT", "Fullscreen Exit"),
        ("NO_FACE", "No Face Detected"),
        ("MULTIPLE_FACE", "Multiple Faces Detected"),
    )

    SEVERITY_CHOICES = (
        ("INFO", "Info"),
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="proctoring_events"
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="proctoring_events"
    )

    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPES
    )

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES,
        default="INFO"
    )

    message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.student.roll_number} - "
            f"{self.exam.exam_name} - "
            f"{self.event_type}"
        )
        