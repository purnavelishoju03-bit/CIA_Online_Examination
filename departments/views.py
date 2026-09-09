from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from .forms import DepartmentForm

def department_list(request):
    departments = Department.objects.all()
    return render(
        request,
        "departments/department_list.html",
        {"departments": departments},
    )


def department_create(request):
    form = DepartmentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("department_list")

    return render(
        request,
        "departments/department_create.html",
        {"form": form},
    )


def department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(request.POST or None, instance=department)

    if form.is_valid():
        form.save()
        return redirect("department_list")

    return render(
        request,
        "departments/department_edit.html",
        {"form": form, "department": department},
    )


def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)

    if request.method == "POST":
        department.delete()
        return redirect("department_list")

    return render(
        request,
        "departments/department_delete.html",
        {"department": department},
    )