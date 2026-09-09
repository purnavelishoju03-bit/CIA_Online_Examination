from django import forms

from .models import Question
from subjects.models import Subject


# ============================================================
# EXCEL UPLOAD FORM
# ============================================================

class ExcelUploadForm(forms.Form):

    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        empty_label="Select Subject",
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    excel_file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "accept": ".xlsx"
            }
        )
    )

    def clean_excel_file(self):

        file = self.cleaned_data["excel_file"]

        if not file.name.lower().endswith(".xlsx"):
            raise forms.ValidationError(
                "Only .xlsx Excel files are allowed."
            )

        return file


# ============================================================
# QUESTION FORM
# ============================================================

class QuestionForm(forms.ModelForm):

    class Meta:

        model = Question

        fields = [
            "subject",
            "question",
            "question_image",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "correct_answer",
            "marks",
            "difficulty",
            "status",
            "question_type",
        ]

        widgets = {

            "subject": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "question": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter question"
                }
            ),

            "question_image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*"
                }
            ),

            "option_a": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Option A"
                }
            ),

            "option_b": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Option B"
                }
            ),

            "option_c": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Option C"
                }
            ),

            "option_d": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Option D"
                }
            ),

            "correct_answer": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "marks": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1"
                }
            ),

            "difficulty": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "question_type": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
        }