from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam
from .forms import ExamForm



def exam_list(request):

    exams = Exam.objects.select_related(
        "department",
        "course",
        "subject",
        "faculty"
    ).all()

    return render(
        request,
        "exams/exams_index.html",
        {
            "exams": exams
        }
    )




def exam_create(request):

    form = ExamForm(request.POST or None)


    if form.is_valid():

        form.save()

        return redirect("exam_list")



    return render(
        request,
        "exams/exams_form.html",
        {
            "form": form,
            "title": "Add Exam"
        }
    )





def exam_edit(request, pk):

    exam = get_object_or_404(
        Exam,
        pk=pk
    )


    form = ExamForm(
        request.POST or None,
        instance=exam
    )


    if form.is_valid():

        form.save()

        return redirect("exam_list")



    return render(
        request,
        "exams/exams_form.html",
        {
            "form": form,
            "title": "Edit Exam"
        }
    )






def exam_delete(request, pk):

    exam = get_object_or_404(
        Exam,
        pk=pk
    )


    if request.method == "POST":

        exam.delete()

        return redirect("exam_list")



    return render(
        request,
        "exams/exams_delete.html",
        {
            "exam": exam,
            "title": "Delete Exam"
        }
    )