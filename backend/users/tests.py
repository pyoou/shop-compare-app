from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUsersNewUser(TestCase):

    def test_user_instance(self):
        db = get_user_model()
        user = db.objects.create_superuser('test@user.com', 'firstname', '123123123', 'password')

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)

        self.assertEqual(str(user), 'test@user.com')

        with self.assertRaises(ValueError):
            db.objects.create_superuser('', 'firstname', 'password')

        with self.assertRaises(ValueError):
            db.objects.create_superuser('test@user.com', 'firstname', 'password', is_staff=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser('test@user.com', 'firstname', 'password', is_superuser=False)