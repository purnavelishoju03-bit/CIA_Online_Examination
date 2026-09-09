from django import forms
from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:

        model = Course

        fields = [
            "department",
            "name",
            "code",
            "duration",
        ]

        widgets = {

            "department": forms.Select(attrs={
                "class": "w-full border rounded-lg px-4 py-2"
            }),

            "name": forms.TextInput(attrs={
                "class": "w-full border rounded-lg px-4 py-2",
                "placeholder": "Course Name"
            }),

            "code": forms.TextInput(attrs={
                "class": "w-full border rounded-lg px-4 py-2",
                "placeholder": "Course Code"
            }),

            "duration": forms.NumberInput(attrs={
                "class": "w-full border rounded-lg px-4 py-2",
                "placeholder": "Course Duration"
            }),
        }