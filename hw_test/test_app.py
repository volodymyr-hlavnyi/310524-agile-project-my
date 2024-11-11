import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.users.models import User
from apps.users.serializers import UserListSerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_list(db):
    return [
        User.objects.create(username='user1', email='user1@example.com'),
        User.objects.create(username='user2', email='user2@example.com')
    ]

@pytest.mark.django_db
def test_get_all_users(api_client, user_list):
    url = reverse('user-list')
    response = api_client.get(url)
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data

@pytest.mark.django_db
def test_get_empty_user_list(api_client, mocker):
    url = reverse('user-list')
    mocker.patch('agile_projects.models.User.objects.all', return_value=User.objects.none())
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == []

@pytest.mark.django_db
def test_create_user(api_client):
    url = reverse('user-list')
    data = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'newpassword123'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(username='newuser').exists()