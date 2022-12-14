import unittest

from src.interpreter import Eva
from test.utils import Run

class TestRecursion(unittest.TestCase):
    def setUp(self):
        pass

    def test_factorial(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
          (begin
            (def factorial (x)
              (if (= x 1) 
                1 
                (* x (factorial (- x 1)))
              )
            )

            (factorial 4)
          )'''
        )

        self.assertEqual(result, 24)