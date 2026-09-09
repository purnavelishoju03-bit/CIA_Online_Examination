from django.urls import path
from . import views

urlpatterns = [

    path(
        "student-login/",
        views.student_login,
        name="student_login"
   

    path("admin-login/",
     views.admin_login,
      name="admin_login"),

]