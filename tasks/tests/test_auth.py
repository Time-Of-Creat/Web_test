from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Task

User = get_user_model()


class TaskAuthTest(TestCase):
    def test_user_can_register(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())