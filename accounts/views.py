from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import StudentLoginForm
from .forms import AdminLoginForm

def home(request):
    return render(request, "accounts/home.html")


def student_login(request):

    form = StudentLoginForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect("student_dashboard")

            else:

                messages.error(
                    request,
                    "Invalid Username or Password"
                )

    return render(
        request,
        "accounts/student_login.html",
        {
            "form": form
        }
    )
def admin_login(request):

    form = AdminLoginForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None and user.is_superuser:

                login(request, user)

                return redirect("dashboard")   # Admin Dashboard

            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(
        request,
        "accounts/admin_login.html",
        {
            "form": form
        }
    )