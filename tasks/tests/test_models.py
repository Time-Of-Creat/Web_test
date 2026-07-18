from django.test import TestCase
from ..models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.task: Task = Task.objects.create(
            title="Купить хлеб",
            completed=False
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Купить хлеб")
        self.assertFalse(self.task.completed)
        self.assertIsNotNone(self.task.creation_date)

    def test_str_method(self):
        self.assertEqual(str(self.task), "Купить хлеб")
