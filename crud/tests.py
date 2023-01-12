from django.test import TestCase
from .utils import validateEmail

# Create your tests here.
class TestEmails(TestCase):
    def test_email_validation_without_at(self):
        errors = validateEmail('test#user.com')
        self.assertIsInstance(errors, list)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'The email must contain "@"!')

    def test_email_validation_with_wrong_domain(self):
        errors = validateEmail('test@com')
        self.assertIsInstance(errors, list)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'The email has no valid format!')
