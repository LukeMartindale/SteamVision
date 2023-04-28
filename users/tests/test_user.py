from django.test import TestCase

class TestTestCase(TestCase):

    def setUp(self):
        self.setUp_test = "This is a setup test"

    def test_tests_are_working(self):
        self.assertEqual(self.setUp_test, "This is a setup test")