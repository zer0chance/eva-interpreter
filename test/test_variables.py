import unittest
from src.eva import Eva

class TestVariables(unittest.TestCase):
    def setUp(self):
        pass

    def test_preinstalls(self):
        eva = Eva()
        self.assertEqual(eva.eval('true'), True)
        self.assertEqual(eva.eval('false'), False)
        self.assertEqual(eva.eval('null'), None)

    def test_variables(self):
        eva = Eva()
        self.assertEqual(eva.eval(['var', 'x', 5]), 5)
        self.assertEqual(eva.eval('x'), 5)

        self.assertRaises(Exception, lambda: eva.eval('y'))
