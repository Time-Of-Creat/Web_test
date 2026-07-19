from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from ..models import Task

User = get_user_model()


class TaskUpdateDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        self.task = Task.objects.create(
            title="Тестовая задача", 
            completed=False,
            user=self.user
        )
    
    def test_update_view_post(self):
        response = self.client.post(reverse('task_update', args=[self.task.pk]), {
            'title': "Обновленная задача",
            'completed': True
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Обновленная задача")
        self.assertTrue(self.task.completed)

    def test_delete_view_post(self):
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
