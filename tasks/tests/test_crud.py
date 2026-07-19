from django.test import TestCase
from django.urls import reverse

from tasks.models import Task


class TaskUpdateDeleteViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Тестовая задача", completed=False)
    
    def test_update_view_post(self):
        response = self.client.post(reverse('task_update', args=[self.task.pk]), {
            'title': "Обновленная задача",
            'completed': True
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Обновленная задача")
        self.assertTrue(self.task.completed)

    def test_delete_view_post(self):
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful delete
        self.assertEqual(Task.objects.count(), 0)
