from django.test import TestCase
from .models import Post
from datetime import datetime
from mock import MagicMock
from django.core.files import File
import tempfile


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(
            title='first post title',
            date=datetime(2015, 10, 9, 23, 55, 59),
            link='http://localhost:8000/post',
            description='first post description',
            tags={'key': 'value'},
            author_email='username@naver.com',
            content_format='markdown',
            content='### first post markdown format content',
            canonical_url='http://localhost:8000/post',
            public_status='private',
            notify_followers=False
        )

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'first post title')

    def test_link_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.link}'
        self.assertEqual(expected_object_name, 'http://localhost:8000/post')

    def test_description_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.description}'
        self.assertEqual(expected_object_name, 'first post description')

    def test_tags_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.tags}'
        self.assertEqual(expected_object_name, "{'key': 'value'}")

    def test_author_email_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.author_email}'
        self.assertEqual(expected_object_name, 'username@naver.com')

    def test_content_format_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.content_format}'
        self.assertEqual(expected_object_name, 'markdown')

    def test_content_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.content}'
        self.assertEqual(expected_object_name,
                         '### first post markdown format content')

    def test_canonical_url_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.canonical_url}'
        self.assertEqual(expected_object_name, 'http://localhost:8000/post')

    def test_public_status_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.public_status}'
        self.assertEqual(expected_object_name, 'private')

    def test_notify_followers_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.notify_followers}'
        self.assertEqual(expected_object_name, 'False')
