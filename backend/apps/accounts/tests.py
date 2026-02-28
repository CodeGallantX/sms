import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        email='test@example.com',
        username='testuser',
        password='password123',
        role='STUDENT'
    )
    assert user.email == 'test@example.com'
    assert user.role == 'STUDENT'
    assert user.check_password('password123')

@pytest.mark.django_db
def test_user_api():
    client = APIClient()
    response = client.post('/api/v1/accounts/users/', {
        'email': 'api@example.com',
        'username': 'apiuser',
        'password': 'password123',
        'first_name': 'API',
        'last_name': 'User',
        'role': 'STUDENT'
    })
    assert response.status_code == 201
    assert response.data['email'] == 'api@example.com'
