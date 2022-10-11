import unittest

from src.interpreter import Eva
from test.utils import Run

class TestLambdaFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_lambda(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
          (begin
            (def event (callback) (begin
              (var x 10)
              (var y 20)
              (callback (+ x y)))
            )

            (event (lambda (data) (* data 10)))
          )'''
        )

        self.assertEqual(result, 300)

    def test_immediate_invocation(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
          ((lambda (x) (* x x)) 5)
          '''
        )

        self.assertEqual(result, 25)

    def test_lambda_assignment(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
          (begin
            (var fun (lambda (x) (* x x)))
            (fun 5)
          )
          '''
        )

        self.assertEqual(result, 25)