from django.shortcuts import render, redirect, get_object_or_404

from .models import Subject
from .forms import SubjectForm


# Subject List
def subject_list(request):

    subjects = Subject.objects.select_related(
        "department",
        "course"
    ).all()

    return render(
        request,
        "subjects/subject_list.html",
        {
            "subjects": subjects
        }
    )


# Add Subject
def subject_create(request):

    form = SubjectForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect("subject_list")

    return render(
        request,
        "subjects/subject_create.html",
        {
            "form": form
        }
    )


# Edit Subject
def subject_edit(request, pk):

    subject = get_object_or_404(
        Subject,
        pk=pk
    )

    form = SubjectForm(
        request.POST or None,
        instance=subject
    )

    if form.is_valid():

        form.save()

        return redirect("subject_list")

    return render(
        request,
        "subjects/subject_edit.html",
        {
            "form": form
        }
    )


# Delete Subject
def subject_delete(request, pk):

    subject = get_object_or_404(
        Subject,
        pk=pk
    )

    if request.method == "POST":

        subject.delete()

        return redirect("subject_list")


    return render(
        request,
        "subjects/subject_delete.html",
        {
            "subject": subject
        }
    )