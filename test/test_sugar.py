import unittest

from src.eva import Eva
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