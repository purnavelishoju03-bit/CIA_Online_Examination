from django import forms
from .models import Exam


class ExamForm(forms.ModelForm):

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        initial="Active",
        widget=forms.Select(attrs={
            "class": "w-full border rounded-lg px-4 py-3"
        })
    )


    class Meta:

        model = Exam

        fields = [
            "exam_name",
            "department",
            "course",
            "semester",
            "subject",
            "faculty",
            "total_marks",
            "pass_marks",
            "exam_date",
            "start_time",
            "end_time",
            "duration",
            "instructions",
            "status",
        ]


        widgets = {

            "exam_name": forms.TextInput(attrs={
                "class": "w-full border rounded-lg px-4 py-3"
            }),


            "department": forms.Select(attrs={
                "class": "w-full border rounded-lg px-4 py-3"
            }),


            "course": forms.Select(attrs={
                "class": "w-full border rounded-lg px-4 py-3"
            }),


            "semester": forms.NumberInput(attrs={
                "class": "w-full border rounded-lg px-4 py-3"
            }),


            "subject": forms.Select(attrs={
                "class": "w-full border rounded-lg px-4 py-3"
            }),


            "faculty": forms.Select(attrs={
                "class": "w-full border rounded-lg px-4 py-3"
            }),


            "total_marks": forms.NumberInput(attrs={
                "class": "w-full border rounded-lg px-4 py-3"
            }),


            "pass_marks": forms.NumberInput(attrs={
                "class": "w-full border rounded-lg px-4 py-3"
            }),


            "exam_date": forms.DateInput(attrs={
                "class": "w-full border rounded-lg px-4 py-3",
                "type": "date"
            }),


            "start_time": forms.TimeInput(attrs={
                "class": "w-full border rounded-lg px-4 py-3",
                "type": "time"
            }),


            "end_time": forms.TimeInput(attrs={
                "class": "w-full border rounded-lg px-4 py-3",
                "type": "time"
            }),


            "duration": forms.NumberInput(attrs={
                "class": "w-full border rounded-lg px-4 py-3"
            }),


            "instructions": forms.Textarea(attrs={
                "class": "w-full border rounded-lg px-4 py-3",
                "rows": 4
            }),

        }