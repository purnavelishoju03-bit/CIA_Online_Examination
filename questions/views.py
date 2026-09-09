import os
import openpyxl

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from django.core.files import File

from .models import Question
from .forms import ExcelUploadForm

from courses.models import Course
from subjects.models import Subject


# ============================================================
# UPLOAD QUESTIONS FROM EXCEL
# ============================================================

def question_upload_excel(request):

    if request.method == "POST":

        form = ExcelUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            subject = form.cleaned_data["subject"]
            excel_file = form.cleaned_data["excel_file"]

            # --------------------------------------------------
            # READ EXCEL
            # --------------------------------------------------

            try:

                workbook = openpyxl.load_workbook(
                    excel_file,
                    data_only=True
                )

                sheet = workbook.active

            except Exception:

                messages.error(
                    request,
                    "Unable to read the Excel file."
                )

                return redirect(
                    "question_upload_excel"
                )

            count = 0
            errors = []

            # ==================================================
            # PROCESS EACH ROW
            # ==================================================

            for row_number, row in enumerate(
                sheet.iter_rows(
                    min_row=2,
                    values_only=True
                ),
                start=2
            ):

                # ------------------------------------------------
                # Skip empty rows
                # ------------------------------------------------

                if not row:
                    continue

                if not row[0] and len(row) < 10:
                    continue

                # =================================================
                # COLUMN A - QUESTION
                # =================================================

                question_text = (
                    str(row[0]).strip()
                    if len(row) > 0 and row[0]
                    else ""
                )

                # =================================================
                # COLUMN B - OPTION A
                # =================================================

                option_a = (
                    str(row[1]).strip()
                    if len(row) > 1 and row[1]
                    else ""
                )

                # =================================================
                # COLUMN C - OPTION B
                # =================================================

                option_b = (
                    str(row[2]).strip()
                    if len(row) > 2 and row[2]
                    else ""
                )

                # =================================================
                # COLUMN D - OPTION C
                # =================================================

                option_c = (
                    str(row[3]).strip()
                    if len(row) > 3 and row[3]
                    else ""
                )

                # =================================================
                # COLUMN E - OPTION D
                # =================================================

                option_d = (
                    str(row[4]).strip()
                    if len(row) > 4 and row[4]
                    else ""
                )

                # =================================================
                # COLUMN F - CORRECT ANSWER
                # =================================================

                correct_answer = (
                    str(row[5]).strip().upper()
                    if len(row) > 5 and row[5]
                    else ""
                )

                # =================================================
                # COLUMN G - MARKS
                # =================================================

                marks = (
                    row[6]
                    if len(row) > 6 and row[6]
                    else 1
                )

                try:

                    marks = int(marks)

                    if marks < 1:
                        marks = 1

                except (TypeError, ValueError):

                    marks = 1

                # =================================================
                # COLUMN H - DIFFICULTY
                # =================================================

                difficulty = (
                    str(row[7]).strip().title()
                    if len(row) > 7 and row[7]
                    else "Medium"
                )

                if difficulty not in [
                    "Easy",
                    "Medium",
                    "Hard"
                ]:

                    difficulty = "Medium"

                # =================================================
                # COLUMN I - QUESTION TYPE
                # =================================================

                question_type = (
                    str(row[8]).strip().upper()
                    if len(row) > 8 and row[8]
                    else "MCQ"
                )

                # ------------------------------------------------
                # VALID QUESTION TYPES
                # ------------------------------------------------

                valid_types = [
                    "MCQ",
                    "VOICE",
                    "IMAGE"
                ]

                if question_type not in valid_types:

                    errors.append(
                        f"Row {row_number}: "
                        f"Invalid Question Type '{question_type}'. "
                        f"Use MCQ, VOICE or IMAGE."
                    )

                    continue

                # =================================================
                # COLUMN J - IMAGE FILE NAME
                # =================================================

                image_name = (
                    str(row[9]).strip()
                    if len(row) > 9 and row[9]
                    else ""
                )

                # =================================================
                # VOICE QUESTION
                # =================================================

                if question_type == "VOICE":

                    # Voice questions do not display
                    # question text or options.

                    question_text = question_text

                    option_a = ""
                    option_b = ""
                    option_c = ""
                    option_d = ""

                    correct_answer = ""

                    image_name = ""

                # =================================================
                # IMAGE QUESTION
                # =================================================

                elif question_type == "IMAGE":

                    # Image filename is compulsory

                    if not image_name:

                        errors.append(
                            f"Row {row_number}: "
                            f"Image filename is required "
                            f"for IMAGE question."
                        )

                        continue

                    # Options are compulsory

                    if not option_a:

                        errors.append(
                            f"Row {row_number}: "
                            f"Option A is required."
                        )

                        continue

                    if not option_b:

                        errors.append(
                            f"Row {row_number}: "
                            f"Option B is required."
                        )

                        continue

                    if not option_c:

                        errors.append(
                            f"Row {row_number}: "
                            f"Option C is required."
                        )

                        continue

                    if not option_d:

                        errors.append(
                            f"Row {row_number}: "
                            f"Option D is required."
                        )

                        continue

                    if correct_answer not in [
                        "A",
                        "B",
                        "C",
                        "D"
                    ]:

                        errors.append(
                            f"Row {row_number}: "
                            f"Correct answer must be "
                            f"A, B, C or D."
                        )

                        continue

                # =================================================
                # NORMAL MCQ
                # =================================================

                elif question_type == "MCQ":

                    if not question_text:

                        errors.append(
                            f"Row {row_number}: "
                            f"Question text is required."
                        )

                        continue

                    if not option_a:

                        errors.append(
                            f"Row {row_number}: "
                            f"Option A is required."
                        )

                        continue

                    if not option_b:

                        errors.append(
                            f"Row {row_number}: "
                            f"Option B is required."
                        )

                        continue

                    if not option_c:

                        errors.append(
                            f"Row {row_number}: "
                            f"Option C is required."
                        )

                        continue

                    if not option_d:

                        errors.append(
                            f"Row {row_number}: "
                            f"Option D is required."
                        )

                        continue

                    if correct_answer not in [
                        "A",
                        "B",
                        "C",
                        "D"
                    ]:

                        errors.append(
                            f"Row {row_number}: "
                            f"Correct answer must be "
                            f"A, B, C or D."
                        )

                        continue

                # =================================================
                # CREATE QUESTION
                # =================================================

                try:

                    question = Question.objects.create(

                        subject=subject,

                        question=question_text,

                        option_a=option_a,

                        option_b=option_b,

                        option_c=option_c,

                        option_d=option_d,

                        correct_answer=correct_answer,

                        marks=marks,

                        difficulty=difficulty,

                        status="Active",

                        question_type=question_type,

                    )

                except Exception as e:

                    errors.append(
                        f"Row {row_number}: "
                        f"Unable to create question. {e}"
                    )

                    continue

                # =================================================
                # SAVE IMAGE
                # =================================================

                if (
                    question_type == "IMAGE"
                    and image_name
                ):

                    image_path = os.path.join(
                        settings.MEDIA_ROOT,
                        "questions",
                        image_name
                    )

                    # ------------------------------------------------
                    # Check image exists
                    # ------------------------------------------------

                    if not os.path.exists(image_path):

                        question.delete()

                        errors.append(
                            f"Row {row_number}: "
                            f"Image '{image_name}' was not found."
                        )

                        continue

                    # ------------------------------------------------
                    # Save image to ImageField
                    # ------------------------------------------------

                    try:

                        with open(
                            image_path,
                            "rb"
                        ) as image_file:

                            question.question_image.save(
                                image_name,
                                File(image_file),
                                save=True
                            )

                    except Exception as e:

                        question.delete()

                        errors.append(
                            f"Row {row_number}: "
                            f"Unable to save image '{image_name}'. "
                            f"{e}"
                        )

                        continue

                # ------------------------------------------------
                # Increase successful count
                # ------------------------------------------------

                count += 1

            # =====================================================
            # SHOW ERRORS
            # =====================================================

            for error in errors:

                messages.warning(
                    request,
                    error
                )

            # =====================================================
            # SUCCESS MESSAGE
            # =====================================================

            if count > 0:

                messages.success(
                    request,
                    f"{count} Questions Uploaded Successfully."
                )

            # =====================================================
            # REDIRECT
            # =====================================================

            return redirect(
                "question_list"
            )

    else:

        form = ExcelUploadForm()

    return render(
        request,
        "questions/upload_excel.html",
        {
            "form": form,
            "title": "Upload Questions",
        },
    )


# ============================================================
# QUESTION LIST
# ============================================================

def question_list(request):

    courses = Course.objects.all()

    course_id = request.GET.get(
        "course"
    )

    subject_id = request.GET.get(
        "subject"
    )

    subjects = Subject.objects.none()

    questions = Question.objects.none()

    # --------------------------------------------------------
    # LOAD SUBJECTS
    # --------------------------------------------------------

    if course_id:

        subjects = Subject.objects.filter(
            course_id=course_id
        )

    # --------------------------------------------------------
    # LOAD QUESTIONS
    # --------------------------------------------------------

    if subject_id:

        questions = Question.objects.filter(
            subject_id=subject_id
        ).order_by("-id")

    return render(
        request,
        "questions/questions_index.html",
        {
            "courses": courses,

            "subjects": subjects,

            "questions": questions,

            "selected_course": course_id,

            "selected_subject": subject_id,
        },
    )


# ============================================================
# AJAX LOAD SUBJECTS
# ============================================================

def load_subjects(request):

    course_id = request.GET.get(
        "course"
    )

    subjects = Subject.objects.filter(
        course_id=course_id
    ).values(
        "id",
        "name"
    )

    return JsonResponse(
        list(subjects),
        safe=False
    )


# ============================================================
# VIEW QUESTION
# ============================================================

def question_view(request, id):

    question = get_object_or_404(
        Question,
        id=id
    )

    return render(
        request,
        "questions/questions_view.html",
        {
            "question": question,

            "title": "View Question",
        },
    )


# ============================================================
# DELETE QUESTION
# ============================================================

def question_delete(request, id):

    question = get_object_or_404(
        Question,
        id=id
    )

    if request.method == "POST":

        question.delete()

        messages.success(
            request,
            "Question Deleted Successfully."
        )

        return redirect(
            "question_list"
        )

    return render(
        request,
        "questions/questions_delete.html",
        {
            "question": question,

            "title": "Delete Question",
        },
    )