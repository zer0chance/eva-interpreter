import unittest

from src.eva import Eva
from test.utils import Run

class TestBuiltinFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_math_operations(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
          (begin
            (var x 10)
            (var y 20)
            (+ x y)
          )'''
        )

        self.assertEqual(result, 30)

    def test_print(self):
        eva = Eva()
        print('\nPrinting ...')
        result = Run.SExpression(eva,
          '''
          (begin
            (var x 10)
            (print x)
            (print "Hello world!")
          )'''
        )

        self.assertEqual(result, None)
