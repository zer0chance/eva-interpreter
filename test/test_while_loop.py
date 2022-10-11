import unittest
from src.interpreter import Eva

class TestWhileLoop(unittest.TestCase):
    def setUp(self):
        pass

    def test_while_loop(self):
        eva = Eva()
        self.assertEqual(eva.eval(['begin', 
                                     ['var', 'a', 1],
                                     ['while', ['<', 'a', 10],
                                        ['set', 'a', ['+', 'a', 1]],
                                     ],
                                     'a'
                                  ]), 10)
