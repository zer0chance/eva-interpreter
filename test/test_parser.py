import unittest
from src.eva import Eva
from parser import evaparser

# def evaluateSExpr(env, expr, expected):


class TestMathExpressions(unittest.TestCase):
    def setUp(self):
        pass

    def test_parsing(self):
        eva = Eva()

        code = '''
        (begin
          (var x 10)
          (var y 20)
          (+ (* x 10) y)
        )'''
        expected = 120

        expr = evaparser.parse(code)
        print(expr)
        self.assertEqual(eva.eval(expr), expected)
