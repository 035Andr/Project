"""
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APIClient, \
    force_authenticate, APITestCase, APISimpleTestCase

from todo.models import Project, Todo
from .views import UserModelViewSet
from django.contrib.auth.models import User
from mixer.backend.django import mixer


class TestUserApi(APITestCase):
    url = '/api/users/'

    def setUp(self) -> None:
        pass

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user(self):
        factory = APIRequestFactory()
        request = factory.post(self.url,
                               {'first_name': 'Tim', 'last_name': 'Bert',
                                'password': '123',
                                'email': 'mail@mail.ru'}, format='json')
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestUserViewSet(TestCase):
    url = '/api/users/'

    def test_get_detail(self):
        client = APIClient()
        user = User.objects.create(username='Andr', email='a@v.da',
                                   password='123')
        response = client.get(f'{self.url}{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestTodoViewSet(APITestCase):
    url = '/api/todo/'
    password = '123'

    def setUp(self) -> None:
        self.admin = User.objects.create_superuser('admin', 'admin@mail.ru',
                                                   self.password)

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        project = Project.objects.create(name='Project TESTTT',
                                         repository_url='https://fgtr.com/')
        # project.users.add(self.admin.id)
        # project.save()
        todo = Todo.objects.create(title='Тестовая заметка',
                                   text='Описание тестовой заметки',
                                   project=project,
                                   user=self.admin)
        self.client.login(username=self.admin.username,
                          password=self.password)  # логинимся
        response = self.client.put(f'{self.url}{todo.id}/',
                                   {'title': 'Тестовая заметка 2',
                                    'text': 'Это описание тестовой заметки 2',
                                    'project': project.id,
                                    'user': self.admin.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = Todo.objects.get(id=todo.id)
        self.assertEqual(todo.title, 'Тестовая заметка 2')
        self.assertEqual(todo.text, 'Это описание тестовой заметки 2')
        self.client.logout()
"""