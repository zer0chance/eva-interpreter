import unittest

from src.eva import Eva
from test.utils import Run

class TestUserFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_function_one_arg(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
          (begin
            (def square (x)
              (* x x)
            )
            (var y 6)
            (square y)
          )'''
        )

        self.assertEqual(result, 36)

    def test_function_two_args(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
          (begin
            (def max (a b)
              (if (> a b) a b)
            )
            (var x 16)
            (var y 5)
            (max x y)
          )'''
        )

        self.assertEqual(result, 16)

    def test_closure(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
          (begin
            (var value 100)
            (def calc (x y)
              (begin
                (var z (+ x y))

                (def inner (p)
                  (+ (+ p z) value)
                )

                inner
              )
            )

            (var fn (calc 10 20))
            (fn 30)
          )'''
        )

        self.assertEqual(result, 160)
