import unittest

from src.eva import Eva
from test.utils import Run

class TestParsing(unittest.TestCase):
    def setUp(self):
        pass

    def test_parsing(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
          (begin
            (var x 10)
            (var y 20)
            (+ (* x 10) y)
          )'''
        )

        self.assertEqual(result, 120)
