import unittest
from Tasks.MoleculeToAtoms import MyClass


class MoleculeToAtoms_Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_molecule(self):
        self.var = 'K4[ON(SO3)2]2'
        self.assertIsInstance(MyClass().parse(self.var), dict)
        self.assertEqual(MyClass().parse(self.var), {'K': 4, 'O': 14, 'N': 2, 'S': 4})
        self.assertEqual(MyClass().parse('Mg(OH)2'), {'Mg': 1, 'O': 2, 'H': 2})
        self.assertNotEqual(MyClass().parse('Mg(OH)2'), {'Mg': 2, 'O': 2, 'H': 2})
        self.assertRaises(TypeError, MyClass().parse, ['K4[ON(SO3)2]2'] )


if __name__ == '__main__':
    unittest.main()
