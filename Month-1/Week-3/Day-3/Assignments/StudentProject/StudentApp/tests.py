from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Student

class StudentAPITests(APITestCase):
    def test_create_student(self):
        url = reverse('student-list')
        data = {
            "name": "Alice",
            "email": "alice@example.com",
            "phone": "9876543210",
            "course": "Django"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Alice")

    def test_get_all_students(self):
        # Create a student record first
        Student.objects.create(
            name="Bob",
            email="bob@example.com",
            phone="1122334455",
            course="Python"
        )
        url = reverse('student-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should be a list (no pagination on Day 3)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Bob")

