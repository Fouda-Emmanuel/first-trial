from django.test import SimpleTestCase
from ourlogic import is_even, multiply


class TestEven(SimpleTestCase):

    def test_even(self):

        result = is_even(4)

        self.assertEqual(result, True)
    
    def test_multiply(self):
        res = multiply(5, 4)
        self.assertEqual(res, 20)