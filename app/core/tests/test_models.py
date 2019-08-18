from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def semple_user(emial='test@test.tt', password='Qwerty12345'):
    return get_user_model().objects.create_user(emial, password)



class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.tt'
        password = 'Qwerty12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email dor a new user is normalize"""
        email = 'test@TEST.tt'
        user = get_user_model().objects.create_user(email, 'Qwerty12345')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Qwerty12345')

    def test_create_new_superuser(self):
        """Testing created a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.tt',
            'Qwerty12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag sting representation"""
        tag = models.Tag.objects.create(
            user=semple_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
