import unittest

from src.interpreter import Eva
from test.utils import Run

class TestModules(unittest.TestCase):
    def setUp(self):
        pass

    def test_module(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
            (module Math
              (begin
                (def abs (x) 
                  (if (> x 0) x (- 0 x))
                )

                (def square (x)
                  (* x x)
                )

                (var MAX_VALUE 10000)
              )
            )

            ((prop Math square) 5)
          '''
        )

        self.assertEqual(result, 25)

    def test_import(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
            (import Math)

            ((prop Math square) 5)
          '''
        )

        self.assertEqual(result, 25)