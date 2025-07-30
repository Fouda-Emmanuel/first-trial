from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):

        email = 'test@test.com'
        password = 'test123'

        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):

        email = 'test@test.com'
        password = 'test123'

        user = get_user_model().objects.create_superuser(email, password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_email_normalize(self):
        sample_email = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@EXAMPLE.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@Example.COM', 'test4@example.com'],
        ]

        for input_email, expected_email in sample_email:
            user = get_user_model().objects.create_user(
                email=input_email, password='test123')

            self.assertEqual(user.email, expected_email)

    def test_user_with_no_email(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')
