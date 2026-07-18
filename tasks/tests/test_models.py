from django.test import TestCase

from ..exceptions import TaskAlreadyCompletedError
from ..models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.task: Task = Task.objects.create(
            title="Купить хлеб",
            completed=False
        )
        self.task_already_completed: Task = Task.objects.create(
            title="Написать модель задачи",
            completed=True
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Купить хлеб")
        self.assertFalse(self.task.completed)
        self.assertIsNotNone(self.task.creation_date)

    def test_str_method(self):
        self.assertEqual(str(self.task), "Купить хлеб")

    def test_complete_method(self):
        self.task.complete()
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

    def test_complete_already_completed_raises_error(self):
        with self.assertRaises(TaskAlreadyCompletedError):
            self.task_already_completed.complete()
