import unittest
from load_balancer import cost_calculate

class Test_Load_Balancer(unittest.TestCase):
    def setUp(self):
        self.total_cost = 0

    def test_return_15(self):
        self.assertEqual(15, cost_calculate(self.total_cost,[5,5,5]))


if __name__ == '__main__':
    unittest.main()
