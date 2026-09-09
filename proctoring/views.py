from django.http import JsonResponse
from django.views.decorators.http import require_POST

from students.models import Student
from exams.models import Exam
from .models import ProctoringEvent


@require_POST
def log_proctoring_event(request):

    student_id = request.POST.get("student_id")
    exam_id = request.POST.get("exam_id")
    event_type = request.POST.get("event_type")
    severity = request.POST.get("severity", "INFO")
    message = request.POST.get("message", "")

    if not student_id or not exam_id or not event_type:
        return JsonResponse(
            {
                "success": False,
                "message": "Missing required data."
            },
            status=400
        )

    try:
        student = Student.objects.get(id=student_id)
        exam = Exam.objects.get(id=exam_id)
    except (Student.DoesNotExist, Exam.DoesNotExist):
        return JsonResponse(
            {
                "success": False,
                "message": "Student or exam not found."
            },
            status=404
        )

    event = ProctoringEvent.objects.create(
        student=student,
        exam=exam,
        event_type=event_type,
        severity=severity,
        message=message
    )

    return JsonResponse({
        "success": True,
        "event_id": event.id
    })