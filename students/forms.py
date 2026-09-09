from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "roll_number",
            "first_name",
            "last_name",
            "department",
            "course",
            "semester",
            "is_active",
        ]

        widgets = {

            # ==============================
            # ROLL NUMBER
            # ==============================

            "roll_number": forms.TextInput(
                attrs={
                    "class": (
                        "w-full h-12 px-4 "
                        "border border-gray-300 "
                        "rounded-lg "
                        "bg-white "
                        "text-gray-800 "
                        "placeholder-gray-400 "
                        "outline-none "
                        "focus:border-blue-500 "
                        "focus:ring-2 "
                        "focus:ring-blue-100 "
                        "transition"
                    ),
                    "placeholder": "Enter roll number",
                    "autocomplete": "off",
                }
            ),

            # ==============================
            # FIRST NAME
            # ==============================

            "first_name": forms.TextInput(
                attrs={
                    "class": (
                        "w-full h-12 px-4 "
                        "border border-gray-300 "
                        "rounded-lg "
                        "bg-white "
                        "text-gray-800 "
                        "placeholder-gray-400 "
                        "outline-none "
                        "focus:border-blue-500 "
                        "focus:ring-2 "
                        "focus:ring-blue-100 "
                        "transition"
                    ),
                    "placeholder": "Enter first name",
                    "autocomplete": "off",
                }
            ),

            # ==============================
            # LAST NAME
            # ==============================

            "last_name": forms.TextInput(
                attrs={
                    "class": (
                        "w-full h-12 px-4 "
                        "border border-gray-300 "
                        "rounded-lg "
                        "bg-white "
                        "text-gray-800 "
                        "placeholder-gray-400 "
                        "outline-none "
                        "focus:border-blue-500 "
                        "focus:ring-2 "
                        "focus:ring-blue-100 "
                        "transition"
                    ),
                    "placeholder": "Enter last name",
                    "autocomplete": "off",
                }
            ),

            # ==============================
            # DEPARTMENT
            # ==============================

            "department": forms.Select(
                attrs={
                    "class": (
                        "w-full h-12 px-4 "
                        "border border-gray-300 "
                        "rounded-lg "
                        "bg-white "
                        "text-gray-800 "
                        "outline-none "
                        "focus:border-blue-500 "
                        "focus:ring-2 "
                        "focus:ring-blue-100 "
                        "transition "
                        "cursor-pointer"
                    ),
                }
            ),

            # ==============================
            # COURSE
            # ==============================

            "course": forms.Select(
                attrs={
                    "class": (
                        "w-full h-12 px-4 "
                        "border border-gray-300 "
                        "rounded-lg "
                        "bg-white "
                        "text-gray-800 "
                        "outline-none "
                        "focus:border-blue-500 "
                        "focus:ring-2 "
                        "focus:ring-blue-100 "
                        "transition "
                        "cursor-pointer"
                    ),
                }
            ),

            # ==============================
            # SEMESTER
            # ==============================

            "semester": forms.NumberInput(
                attrs={
                    "class": (
                        "w-full h-12 px-4 "
                        "border border-gray-300 "
                        "rounded-lg "
                        "bg-white "
                        "text-gray-800 "
                        "placeholder-gray-400 "
                        "outline-none "
                        "focus:border-blue-500 "
                        "focus:ring-2 "
                        "focus:ring-blue-100 "
                        "transition"
                    ),
                    "placeholder": "Enter semester",
                    "min": "1",
                    "max": "10",
                }
            ),

            # ==============================
            # ACTIVE
            # ==============================

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": (
                        "w-5 h-5 "
                        "text-blue-600 "
                        "border-gray-300 "
                        "rounded "
                        "focus:ring-blue-500"
                    ),
                }
            ),
        }