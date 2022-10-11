import unittest
from src.interpreter import Eva

class TestIfStatement(unittest.TestCase):
    def setUp(self):
        pass

    def test_if_statement(self):
        eva = Eva()
        self.assertEqual(eva.eval(['begin', 
                                     ['var', 'a', 1],
                                     ['var', 'b', 10],
                                     ['if', ['<', 'a', 'b'],
                                        ['set', 'a', 20],
                                        ['set', 'a', 40],
                                     ],
                                     'a'
                                  ]), 20)