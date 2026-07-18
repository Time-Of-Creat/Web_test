from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("new/", views.TaskCreateView.as_view(), name="task_create")
]
