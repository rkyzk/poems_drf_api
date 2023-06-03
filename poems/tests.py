from django.contrib.auth.models import User
from .models import Poem
from rest_framework import status
from rest_framework.test import APITestCase


class PoemListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='user', password='pass')

    def test_can_list_posts(self):
        user = User.objects.get(username='user')
        Poem.objects.create(owner=user, title='test')
        response = self.client.get('/poems/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)
        # print(len(response.data))

    def test_logged_in_user_can_create_poem(self):
        self.client.login(username='user', password='pass')
        response = self.client.post(
            '/poems/',
            {'title': 'test',
             'content': 'content'}
            )
        count = Poem.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_poem(self):
        response = self.client.post('/poems/', {'title': 'test'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
