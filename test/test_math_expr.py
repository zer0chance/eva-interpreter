import unittest
from src.eva import Eva

class TestMathExpressions(unittest.TestCase):
    def setUp(self):
        pass

    def test_math(self):
        eva = Eva()
        self.assertEqual(eva.eval(['+', 3, 4]), 7)
        self.assertEqual(eva.eval(['+', ['+', 5, -4], 9]), 10)

        self.assertEqual(eva.eval(['-', 5, 2]), 3)
        self.assertEqual(eva.eval(['-', ['+', 15, -4], 9]), 2)

        self.assertEqual(eva.eval(['*', 3, 4]), 12)
        self.assertEqual(eva.eval(['*', 3, ['+', 2, 1]]), 9)

        self.assertEqual(eva.eval(['/', 8, 2]), 4)
        self.assertEqual(eva.eval(['/', ['-', 10, 1], 2]), 4.5)

        self.assertEqual(eva.eval(['%', 6, 4]), 2)
        self.assertEqual(eva.eval(['%', ['-', 10, 1], 2]), 1)
