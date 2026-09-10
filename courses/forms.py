
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
            "department": forms.Select(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-gray-400",
                }
            ),

            "name": forms.TextInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-gray-400",
                    "placeholder": "Course Name",
                }
            ),

            "code": forms.TextInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-gray-400",
                    "placeholder": "Course Code",
                }
            ),

            "duration": forms.NumberInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-gray-400",
                    "placeholder": "Course Duration in Years",
                    "min": "1",
                }
            ),
        }

