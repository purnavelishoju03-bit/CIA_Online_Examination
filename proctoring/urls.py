from django.urls import path

from . import views


urlpatterns = [

    path(
        "log-event/",
        views.log_proctoring_event,
        name="log_proctoring_event"
    ),

]