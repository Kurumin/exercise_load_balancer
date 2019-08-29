import unittest
from load_balance import distribute_users, tick

class TestLoadBalancer(unittest.TestCase):
    def setUp(self):
        self.ttask = 4
        self.umax = 2
        self.servers = [[]]

    def test_iteration_1(self):
        self.assertEqual([[4]], distribute_users(1, tick(self.servers), self.umax, self.ttask))

    def test_iteration_2(self):
        self.assertEqual([[3, 4], [4, 4]], distribute_users(3, tick([[4]]), self.umax, self.ttask))

    def test_iteration_3(self):
        self.assertEqual([[2, 3], [3, 3]], distribute_users(0, tick([[3, 4], [4, 4]]), self.umax, self.ttask))

    def test_iteration_4(self):
        self.assertEqual([[1, 2], [2, 2], [4]], distribute_users(1, tick([[2, 3], [3, 3]]), self.umax, self.ttask))

    def test_iteration_5(self):
        self.assertEqual([[1], [1, 1], [3]], distribute_users(0, tick([[1, 2], [2, 2], [4]]), self.umax, self.ttask))

    def test_iteration_6(self):
        self.assertEqual([[2, 4]], distribute_users(1, tick([[1], [1, 1], [3]]), self.umax, self.ttask))

    def test_iteration_7(self):
        self.assertEqual([[1, 3]], distribute_users(0, tick([[2, 4]]), self.umax, self.ttask))

    def test_iteration_8(self):
        self.assertEqual([[2]], distribute_users(0, tick([[1, 3]]), self.umax, self.ttask))

    def test_iteration_9(self):
        self.assertEqual([[1]], distribute_users(0, tick([[2]]), self.umax, self.ttask))

    def test_iteration_10(self):
        self.assertEqual([], distribute_users(0, tick([[1]]), self.umax, self.ttask))


if __name__ == '__main__':
    unittest.main()
