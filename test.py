import unittest
from random import randint
from main import *


class BoxStackingTest(unittest.TestCase):

    def assert_all_method_results_equal_n(self, d1, d2, d3, n):
        self.assertEqual(maxHeightTry1(d1, d2, d3), n)
        self.assertEqual(maxHeightTry2(d1, d2, d3), n)
        self.assertEqual(maxHeightTry3(d1, d2, d3), n)

    def test_empty(self):
        d1, d2, d3 = [], [], []
        self.assertRaises(
            AssertionError, maxHeightTry1, d1, d2, d3)
        self.assertRaises(
            AssertionError, maxHeightTry2, d1, d2, d3)
        self.assertRaises(
            AssertionError, maxHeightTry3, d1, d2, d3)

    def test_1_element_order1(self):
        d1, d2, d3 = [1], [3], [5]
        self.assert_all_method_results_equal_n(d1, d2, d3, 6)

    def test_1_element_order2(self):
        d1, d2, d3 = [3], [1], [5]
        self.assert_all_method_results_equal_n(d1, d2, d3, 6)

    def test_1_element_order3(self):
        d1, d2, d3 = [5], [3], [1]
        self.assert_all_method_results_equal_n(d1, d2, d3, 6)

    def test_same_dimensions_1(self):
        d1, d2, d3 = [86], [87], [87]
        self.assert_all_method_results_equal_n(d1, d2, d3, 87)

    def test_same_dimensions_2(self):
        d1, d2, d3 = [86], [86], [87]
        self.assert_all_method_results_equal_n(d1, d2, d3, 87)

    def test_same_dimensions_3(self):
        d1, d2, d3 = [86], [86], [86]
        self.assert_all_method_results_equal_n(d1, d2, d3, 86)

    def test_3_elements(self):
        d1, d2, d3 = [1, 4, 3], [2, 5, 4], [3, 6, 1]
        self.assert_all_method_results_equal_n(d1, d2, d3, 15)

    def test_4_elements(self):
        d1, d2, d3 = [4, 1, 4, 32], [6, 2, 5, 12], [7, 3, 6, 10]
        self.assert_all_method_results_equal_n(d1, d2, d3, 60)

    def test_large_example1(self):
        d1, d2, d3 = [27, 52, 29, 89, 78, 100, 88, 58], [
            28, 72, 11, 99, 94, 77, 32, 100], [98, 70, 50, 40, 11, 91, 53, 78]
        self.assert_all_method_results_equal_n(d1, d2, d3, 597)

    def test_large_example2(self):
        d1, d2, d3 = [27, 52, 29, 89, 78, 100, 88, 58, 22, 73, 55, 10, 22, 40], [28, 72, 11, 99, 94, 77,
                                                                                 32, 100, 55, 33, 99, 51, 23, 8], [98, 70, 50, 40, 11, 91, 53, 78, 48, 65, 33, 71, 103, 151]
        self.assert_all_method_results_equal_n(d1, d2, d3, 817)

    def test_very_large_example(self):
        d1, d2, d3 = [16, 87, 22, 91, 27, 73, 69, 83, 24, 30, 59, 94, 43, 22, 38, 16, 27, 57, 71, 6, 28, 47, 58, 83, 68, 44, 9, 89, 52, 33, 69, 27, 40, 35], [78, 36, 50, 28, 64, 27, 12, 30, 63, 36, 23, 68, 12, 74, 85,
                                                                                                                                                              25, 14, 81, 63, 82, 85, 6, 14, 96, 15, 65, 88, 79, 4, 100, 77, 13, 95, 71], [87, 94, 93, 63, 60, 41, 37, 68, 31, 68, 3, 70, 57, 30, 20, 99, 71, 92, 74, 97, 26, 37, 30, 25, 46, 35, 51, 77, 85, 55, 61, 40, 87, 96]
        self.assert_all_method_results_equal_n(d1, d2, d3, 1111)

    def test_same_results_of_random_inputs(self):
        for _ in range(10):
            d1, d2, d3 = [randint(1, 50) for _ in range(100)], [randint(
                1, 50) for _ in range(100)], [randint(1, 50) for _ in range(100)]
            res1 = maxHeightTry1(d1, d2, d3)
            res2 = maxHeightTry2(d1, d2, d3)
            res3 = maxHeightTry3(d1, d2, d3)
            self.assertEqual(res1, res2)
            self.assertEqual(res2, res3)


if __name__ == "__main__":
    unittest.main()
