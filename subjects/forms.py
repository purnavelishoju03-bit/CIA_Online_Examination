from django import forms
from .models import Subject


class SubjectForm(forms.ModelForm):

    class Meta:

        model = Subject

        fields = [
            "department",
            "course",
            "name",
            "code",
            "semester",
            "credits",
            "description",
            "is_active",
        ]

        widgets = {

            "department": forms.Select(attrs={
                "class":"w-full border border-gray-300 rounded-lg px-4 py-2"
            }),

            "course": forms.Select(attrs={
                "class":"w-full border border-gray-300 rounded-lg px-4 py-2"
            }),

            "name": forms.TextInput(attrs={
                "class":"w-full border border-gray-300 rounded-lg px-4 py-2",
                "placeholder":"Subject Name"
            }),

            "code": forms.TextInput(attrs={
                "class":"w-full border border-gray-300 rounded-lg px-4 py-2",
                "placeholder":"Subject Code"
            }),

            "semester": forms.NumberInput(attrs={
                "class":"w-full border border-gray-300 rounded-lg px-4 py-2"
            }),

            "credits": forms.NumberInput(attrs={
                "class":"w-full border border-gray-300 rounded-lg px-4 py-2"
            }),

            "description": forms.Textarea(attrs={
                "class":"w-full border border-gray-300 rounded-lg px-4 py-2",
                "rows":4
            }),

        }