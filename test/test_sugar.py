import unittest

from src.interpreter import Eva
from test.utils import Run

class TestSyntacticSugar(unittest.TestCase):
    def setUp(self):
        pass

    def test_switch(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
          (begin
            (var x 12)
            (switch ((= x 10) 100)
                    ((> x 10) 200)
                    (else     300)
            )
          )'''
        )

        self.assertEqual(result, 200)

    def test_for(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
          (for (var x 1) (< x 10) (set x (+ x 1)) (print x))
          '''
        )

        self.assertEqual(result, 10)
   
    def test_inc_dec(self):
          eva = Eva()

          result = Run.SExpression(eva,
            '''
            (var x 1) 
            (inc x)
            x
            '''
          )
          self.assertEqual(result, 2)

          result = Run.SExpression(eva,
            '''
            (var y 2) 
            (dec y)
            y
            '''
          )
          self.assertEqual(result, 1)
