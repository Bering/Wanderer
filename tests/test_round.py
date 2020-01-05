import unittest

class Test_Template(unittest.TestCase):
    def test_round_to_zero(self):
        self.assertEqual(0, round(0.4))
    

    def test_round_negative_to_zero(self):
        self.assertEqual(0, round(-0.4))

    
    def test_round_to_one(self):
        self.assertEqual(1, round(0.50001))


    def test_round_to_negative_one(self):
        self.assertEqual(-1, round(-0.50001))


if __name__ == '__main__':
    unittest.main()
