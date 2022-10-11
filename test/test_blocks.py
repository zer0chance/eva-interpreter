import unittest
from src.interpreter import Eva

class TestBlocks(unittest.TestCase):
    def setUp(self):
        pass

    def test_block(self):
        eva = Eva()
        self.assertEqual(eva.eval(['begin', 
                                     ['var', 'a', 5],
                                     ['var', 'b', 7],
                                     ['+', 'a', 'b']
                                  ]), 12)

    def test_nested_block(self):
        eva = Eva()
        self.assertEqual(eva.eval(['begin', 
                                     ['var', 'x', 5],
                                     ['begin',
                                        ['var', 'x', 10],
                                     ],
                                     'x'
                                  ]), 5)

    def test_outer_access(self):
        eva = Eva()
        self.assertEqual(eva.eval(['begin', 
                                     ['var', 'outer', 5],
                                     ['var', 'result', ['begin',
                                        ['var', 'inner', ['*', 'outer', 2]]
                                     ]],
                                     'result'
                                  ]), 10)

    def test_outer_set(self):
        eva = Eva()
        self.assertEqual(eva.eval(['begin', 
                                     ['var', 'outer', 5],
                                     ['begin',
                                        ['set', 'outer', 25]
                                     ],
                                     'outer'
                                  ]), 25)