import utils
import unittest

class test_utils(unittest.TestCase):
    def test_most_common_pair(self):
        self.assertEqual(utils.most_common_pair([1,2,3,4,1,2]), (1,2))
        self.assertEqual(utils.most_common_pair([1,2,1,1,1,1,1,1]), (1,1))
        self.assertEqual(utils.most_common_pair([]), ())
        self.assertEqual(utils.most_common_pair([1]), ())
        self.assertEqual(utils.most_common_pair([1,2]),(1,2))
        self.assertEqual(utils.most_common_pair([1,2,3,4,5]), (1,2))

    def test_swapping_most_common_pair(self):
        self.assertEqual(utils.swapping_most_common_pair([1,2,3,4,1,2], (1,2)), [5,3,4,5])
        self.assertEqual(utils.swapping_most_common_pair([1,2,1,1,1,1,1,1,1], (1,1)), [1,2,3,3,3,1])
        self.assertEqual(utils.swapping_most_common_pair([1,2,3,4,5], ()), [1,2,3,4,5])
        self.assertEqual(utils.swapping_most_common_pair([1], ()), [1])
        self.assertEqual(utils.swapping_most_common_pair([], ()), [])

if __name__ == "__main__":

    unittest.main()