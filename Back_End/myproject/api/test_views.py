from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from base.models import User, Court
from django.contrib.auth.hashers import make_password

class APITests(APITestCase):

    def setUp(self):
        self.manager = User.objects.create(
            username='manager',
            password=make_password('password123'),
            is_manager=True
        )
        self.user = User.objects.create(
            username='user',
            password=make_password('password123'),
            is_manager=False
        )
        self.court = Court.objects.create(
            sport='Tennis',
            num=1
        )

    def test_login_with_valid_credentials(self):
        url = reverse('login')
        data = {'username': 'manager', 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Login successful')

    def test_login_with_invalid_credentials(self):
        url = reverse('login')
        data = {'username': 'manager', 'password': 'wrongpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Invalid password')

    def test_reserve_court_with_valid_inputs(self):
        url = reverse('reserve-court')
        data = {'court_id': self.court.id, 'user_id': self.user.id}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Court reserved successfully')

    def test_reserve_court_with_invalid_inputs(self):
        url = reverse('reserve-court')
        data = {'court_id': 999, 'user_id': self.user.id}  # Invalid court_id
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Court is already reserved or does not exist')