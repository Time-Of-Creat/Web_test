from django.db import models
from django.contrib.auth import get_user_model

from tasks.exceptions import TaskAlreadyCompletedError


User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def complete(self):
        if self.completed:
            raise TaskAlreadyCompletedError(f"Задача '{self.title}' уже отмечена как выполненная.")
        self.completed = True
        self.save()
