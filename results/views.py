from django.shortcuts import render
from django.http import HttpResponse

from departments.models import Department
from courses.models import Course
from results.models import Result

from openpyxl import Workbook


# =========================================================
# RESULTS PAGE
# =========================================================

def results_list(request):

    departments = Department.objects.all().order_by("id")
    courses = Course.objects.all().order_by("id")

    selected_department = request.GET.get("department", "")
    selected_course = request.GET.get("course", "")
    selected_semester = request.GET.get("semester", "")

    results = Result.objects.select_related(
        "student",
        "student__department",
        "student__course",
        "exam",
        "exam__subject"
    ).all()

    # -----------------------------------------------------
    # FILTER BY DEPARTMENT
    # -----------------------------------------------------

    if selected_department:
        results = results.filter(
            student__department_id=selected_department
        )

    # -----------------------------------------------------
    # FILTER BY COURSE
    # -----------------------------------------------------

    if selected_course:
        results = results.filter(
            student__course_id=selected_course
        )

    # -----------------------------------------------------
    # FILTER BY SEMESTER
    # -----------------------------------------------------

    if selected_semester:
        results = results.filter(
            student__semester=selected_semester
        )

    results = results.order_by(
        "student__roll_number",
        "-submitted_at"
    )

    context = {
        "departments": departments,
        "courses": courses,
        "results": results,

        "selected_department": selected_department,
        "selected_course": selected_course,
        "selected_semester": selected_semester,

        "total_results": results.count(),
        "passed_results": results.filter(status="Pass").count(),
        "failed_results": results.filter(status="Fail").count(),
    }

    return render(
        request,
        "results/results_list.html",
        context
    )


# =========================================================
# DOWNLOAD RESULTS AS EXCEL
# =========================================================

def export_results_excel(request):

    selected_department = request.GET.get("department", "")
    selected_course = request.GET.get("course", "")
    selected_semester = request.GET.get("semester", "")

    results = Result.objects.select_related(
        "student",
        "student__department",
        "student__course",
        "exam",
        "exam__subject"
    ).all()

    # -----------------------------------------------------
    # APPLY SAME FILTERS
    # -----------------------------------------------------

    if selected_department:
        results = results.filter(
            student__department_id=selected_department
        )

    if selected_course:
        results = results.filter(
            student__course_id=selected_course
        )

    if selected_semester:
        results = results.filter(
            student__semester=selected_semester
        )

    results = results.order_by(
        "student__roll_number"
    )

    # -----------------------------------------------------
    # CREATE EXCEL WORKBOOK
    # -----------------------------------------------------

    workbook = Workbook()

    worksheet = workbook.active
    worksheet.title = "Examination Results"

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    headers = [
        "S.No",
        "Roll Number",
        "Student Name",
        "Department",
        "Course",
        "Semester",
        "Exam",
        "Subject",
        "Obtained Marks",
        "Total Marks",
        "Percentage",
        "Status",
        "Submitted At",
    ]

    worksheet.append(headers)

    # -----------------------------------------------------
    # DATA
    # -----------------------------------------------------

    for index, result in enumerate(results, start=1):

        student = result.student

        student_name = (
            f"{student.first_name} {student.last_name}"
        ).strip()

        worksheet.append([
            index,
            student.roll_number,
            student_name,
            student.department,
            student.course,
            student.semester,
            result.exam.exam_name,
            result.exam.subject,
            result.obtained_marks,
            result.total_marks,
            float(result.percentage),
            result.status,
            result.submitted_at.strftime(
                "%d-%m-%Y %H:%M"
            ) if result.submitted_at else "",
        ])

    # -----------------------------------------------------
    # COLUMN WIDTHS
    # -----------------------------------------------------

    column_widths = {
        "A": 8,
        "B": 18,
        "C": 25,
        "D": 20,
        "E": 20,
        "F": 12,
        "G": 30,
        "H": 20,
        "I": 18,
        "J": 15,
        "K": 15,
        "L": 12,
        "M": 22,
    }

    for column, width in column_widths.items():
        worksheet.column_dimensions[column].width = width

    # -----------------------------------------------------
    # RESPONSE
    # -----------------------------------------------------

    response = HttpResponse(
        content_type=(
            "application/vnd.openxmlformats-officedocument"
            ".spreadsheetml.sheet"
        )
    )

    response["Content-Disposition"] = (
        'attachment; filename="examination_results.xlsx"'
    )

    workbook.save(response)

    return response


# =========================================================
# REPORTS
# =========================================================

def reports_dashboard(request):

    return render(
        request,
        "results/reports_dashboard.html"
    )