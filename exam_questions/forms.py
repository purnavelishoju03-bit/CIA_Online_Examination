from django import forms

from exams.models import Exam
from questions.models import Question

from .models import ExamQuestion


class ExamQuestionForm(forms.ModelForm):

    class Meta:
        model = ExamQuestion

        fields = [
            "exam",
            "question",
            "question_order",
        ]

        widgets = {

            "exam": forms.Select(attrs={
                "class": "form-control"
            }),

            "question": forms.Select(attrs={
                "class": "form-control"
            }),

            "question_order": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 1
            }),

        }


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Exam dropdown
        self.fields["exam"].queryset = Exam.objects.all()


        # Default: no questions
        self.fields["question"].queryset = Question.objects.none()


        # ---------------------------------------------
        # EDIT MAPPING
        # ---------------------------------------------
        if self.instance.pk and self.instance.exam_id:

            self.fields["question"].queryset = Question.objects.filter(
                subject=self.instance.exam.subject,
                status="Active"
            )


            # Keep the current question available
            if self.instance.question_id:

                self.fields["question"].queryset = (
                    self.fields["question"].queryset |
                    Question.objects.filter(
                        id=self.instance.question_id
                    )
                )