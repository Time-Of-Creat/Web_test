from django.test import TestCase
from django.urls import reverse
from ..models import Task


class TaskCreateViewTest(TestCase):
    def test_create_view_get(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_form.html')

    def test_create_view_post(self):
        tasks_count_before = Task.objects.count()

        response = self.client.post(reverse('task_create'), {
            'title': 'Купить много хлеба'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))

        tasks_count_after = Task.objects.count()
        self.assertEqual(tasks_count_after, tasks_count_before + 1)
