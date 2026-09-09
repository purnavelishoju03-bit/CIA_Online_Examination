from django import forms
from django.contrib.auth.models import User

from .models import Faculty


# ============================================================
# FACULTY FORM
# ============================================================

class FacultyForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Enter username"
            }
        )
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Enter password"
            }
        )
    )

    class Meta:

        model = Faculty

        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "department",
            "course",
            "subject",
            "designation",
            "qualification",
            "experience",
            "status",
        ]

        widgets = {

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Enter first name"
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Enter last name"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Enter email address"
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Enter phone number"
                }
            ),

            "department": forms.Select(
                attrs={
                    "class": "form-input"
                }
            ),

            "course": forms.Select(
                attrs={
                    "class": "form-input"
                }
            ),

            "subject": forms.Select(
                attrs={
                    "class": "form-input"
                }
            ),

            "designation": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Example: Assistant Professor"
                }
            ),

            "qualification": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Example: M.Tech / MBA / Ph.D"
                }
            ),

            "experience": forms.NumberInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Years of experience",
                    "min": "0"
                }
            ),

            "status": forms.CheckboxInput(
                attrs={
                    "class": "status-checkbox"
                }
            ),
        }

    def clean_username(self):

        username = self.cleaned_data["username"]

        if User.objects.filter(username=username).exists():

            raise forms.ValidationError(
                "This username is already registered."
            )

        return username


# ============================================================
# FACULTY LOGIN FORM
# ============================================================

class FacultyLoginForm(forms.Form):

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "login-input",
                "placeholder": "Enter username",
                "autocomplete": "username"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "login-input",
                "placeholder": "Enter password",
                "autocomplete": "current-password"
            }
        )
    )