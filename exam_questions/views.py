from django.shortcuts import render, redirect, get_object_or_404

from exams.models import Exam
from questions.models import Question

from .models import ExamQuestion
from .forms import ExamQuestionForm


# =========================================================
# LIST QUESTION MAPPINGS
# =========================================================
def exam_question_list(request):

    questions = ExamQuestion.objects.select_related(
        "exam",
        "question",
        "question__subject"
    ).all().order_by(
        "exam",
        "question_order"
    )

    return render(
        request,
        "exam_questions/exam_questions_index.html",
        {
            "questions": questions,
            "title": "Exam Question Mapping"
        }
    )


# =========================================================
# BULK QUESTION MAPPING
# =========================================================
def exam_question_mapping(request):

    exams = Exam.objects.filter(
        status="Active"
    ).order_by("-id")

    selected_exam = None
    available_questions = Question.objects.none()

    # -----------------------------------------------------
    # Get selected exam
    # -----------------------------------------------------
    exam_id = request.GET.get("exam") or request.POST.get("exam")

    if exam_id:

        selected_exam = get_object_or_404(
            Exam,
            id=exam_id
        )

        # -------------------------------------------------
        # Find questions already mapped to this exam
        # -------------------------------------------------
        mapped_question_ids = ExamQuestion.objects.filter(
            exam=selected_exam
        ).values_list(
            "question_id",
            flat=True
        )

        # -------------------------------------------------
        # Show active questions belonging to exam subject
        # -------------------------------------------------
        available_questions = Question.objects.filter(
            subject=selected_exam.subject,
            status="Active"
        ).exclude(
            id__in=mapped_question_ids
        ).order_by(
            "id"
        )

    # -----------------------------------------------------
    # Save selected questions
    # -----------------------------------------------------
    if request.method == "POST" and selected_exam:

        question_ids = request.POST.getlist(
            "questions"
        )

        if question_ids:

            # Find current highest question order
            last_mapping = ExamQuestion.objects.filter(
                exam=selected_exam
            ).order_by(
                "-question_order"
            ).first()

            if last_mapping:
                next_order = last_mapping.question_order + 1
            else:
                next_order = 1

            # ---------------------------------------------
            # Create mappings
            # ---------------------------------------------
            for question_id in question_ids:

                question = Question.objects.filter(
                    id=question_id,
                    subject=selected_exam.subject,
                    status="Active"
                ).first()

                if not question:
                    continue

                # Avoid duplicate mappings
                if ExamQuestion.objects.filter(
                    exam=selected_exam,
                    question=question
                ).exists():
                    continue

                ExamQuestion.objects.create(
                    exam=selected_exam,
                    question=question,
                    question_order=next_order
                )

                next_order += 1

        return redirect(
            f"/admin-panel/exam-questions/mapping/?exam={selected_exam.id}"
        )

    return render(
        request,
        "exam_questions/exam_questions_mapping.html",
        {
            "exams": exams,
            "selected_exam": selected_exam,
            "available_questions": available_questions,
        },
    )


# =========================================================
# ADD SINGLE QUESTION MAPPING
# =========================================================
def exam_question_add(request):

    exam_id = request.GET.get("exam") or request.POST.get("exam")

    selected_exam = None

    # -----------------------------------------------------
    # If exam is provided, get the exam
    # -----------------------------------------------------
    if exam_id:

        selected_exam = get_object_or_404(
            Exam,
            id=exam_id
        )

    # -----------------------------------------------------
    # POST
    # -----------------------------------------------------
    if request.method == "POST":

        form = ExamQuestionForm(
            request.POST
        )

        # -------------------------------------------------
        # Limit exam choices to active exams
        # -------------------------------------------------
        form.fields["exam"].queryset = Exam.objects.filter(
            status="Active"
        )

        # -------------------------------------------------
        # If exam selected, show only questions belonging
        # to that exam's subject
        # -------------------------------------------------
        if selected_exam:

            form.fields["exam"].initial = selected_exam

            form.fields["question"].queryset = Question.objects.filter(
                subject=selected_exam.subject,
                status="Active"
            )

        if form.is_valid():

            mapping = form.save()

            return redirect(
                "exam_question_list"
            )

    # -----------------------------------------------------
    # GET
    # -----------------------------------------------------
    else:

        form = ExamQuestionForm()

        form.fields["exam"].queryset = Exam.objects.filter(
            status="Active"
        )

        if selected_exam:

            form.fields["exam"].initial = selected_exam

            form.fields["question"].queryset = Question.objects.filter(
                subject=selected_exam.subject,
                status="Active"
            )

    return render(
        request,
        "exam_questions/exam_question_add.html",
        {
            "form": form,
            "selected_exam": selected_exam,
            "title": "Add Exam Question"
        }
    )


# =========================================================
# EDIT QUESTION MAPPING
# =========================================================
def exam_question_edit(request, id):

    mapping = get_object_or_404(
        ExamQuestion,
        id=id
    )

    if request.method == "POST":

        form = ExamQuestionForm(
            request.POST,
            instance=mapping
        )

        # Only allow questions belonging
        # to the exam subject
        form.fields["question"].queryset = Question.objects.filter(
            subject=mapping.exam.subject,
            status="Active"
        )

        if form.is_valid():

            form.save()

            return redirect(
                "exam_question_list"
            )

    else:

        form = ExamQuestionForm(
            instance=mapping
        )

        form.fields["question"].queryset = Question.objects.filter(
            subject=mapping.exam.subject,
            status="Active"
        )

    return render(
        request,
        "exam_questions/exam_questions_form.html",
        {
            "form": form,
            "title": "Edit Mapping"
        }
    )


# =========================================================
# DELETE QUESTION MAPPING
# =========================================================
def exam_question_delete(request, id):

    mapping = get_object_or_404(
        ExamQuestion,
        id=id
    )

    if request.method == "POST":

        mapping.delete()

        return redirect(
            "exam_question_list"
        )

    return render(
        request,
        "exam_questions/exam_questions_delete.html",
        {
            "question": mapping,
            "title": "Delete Mapping"
        }
    )