import unittest

from src.interpreter import Eva
from test.utils import Run

class TestList(unittest.TestCase):
    def setUp(self):
        pass

    def test_list(self):
        eva = Eva()

        result = Run.SExpression(eva,
          '''
            (list l 12 "Hello" 3 "By")
            (print "\n" l)
            (set (idx l 1) "Hello, world!")
            (print " " l)
          '''
        )
        
        self.assertEqual(result, None)
