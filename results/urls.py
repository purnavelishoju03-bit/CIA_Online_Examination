from django.urls import path
from . import views


urlpatterns = [

    # =====================================================
    # RESULTS
    # =====================================================

    path(
        "",
        views.results_list,
        name="results_list"
    ),

    # =====================================================
    # DOWNLOAD EXCEL
    # =====================================================

    path(
        "export-excel/",
        views.export_results_excel,
        name="export_results_excel"
    ),

    # =====================================================
    # REPORTS
    # =====================================================

    path(
        "reports/",
        views.reports_dashboard,
        name="reports_dashboard"
    ),

]