from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("new/", views.TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/edit/", views.TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task_delete"),
    path("<int:pk>/complete/", views.task_complete, name="task_complete"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
