import unittest
from src.interpreter import Eva

class TestSelfEvaluatingExpressions(unittest.TestCase):
    def setUp(self):
        pass

    def test_numbers(self):
        eva = Eva()
        self.assertEqual(eva.eval(1), 1)
        self.assertEqual(eva.eval(3.14), 3.14)
        self.assertEqual(eva.eval(-128), -128)

    def test_strings(self):
        eva = Eva()
        self.assertEqual(eva.eval('""'), "")
        self.assertEqual(eva.eval('"Hello world!"'), "Hello world!")
