from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Student

class StudentAPITests(APITestCase):
    def setUp(self):
        # Create some students for pagination testing (12 records)
        for i in range(12):
            Student.objects.create(
                name=f"Student {i}",
                email=f"student{i}@example.com",
                phone=f"12345678{i:02d}",
                course="Python"
            )

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

    def test_get_students_pagination(self):
        url = reverse('student-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that page 1 has 5 records
        self.assertEqual(len(response.data['results']), 5)
        # Check pagination metadata
        self.assertEqual(response.data['count'], 12)
        self.assertIsNotNone(response.data['next'])

    def test_get_student_detail(self):
        student = Student.objects.first()
        url = reverse('student-detail', kwargs={'pk': student.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], student.name)

    def test_update_student(self):
        student = Student.objects.first()
        url = reverse('student-detail', kwargs={'pk': student.pk})
        data = {"name": "Updated Name"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Name")

    def test_delete_student(self):
        student = Student.objects.first()
        url = reverse('student-detail', kwargs={'pk': student.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Student.objects.filter(pk=student.pk).exists())

