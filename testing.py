import utils
import unittest

class test_utils(unittest.TestCase):
    def test_most_common_pair(self):
        self.assertEqual(utils.most_common_pair([1,2,3,4,1,2]), (1,2))
        self.assertEqual(utils.most_common_pair([1,2,1,1,1,1,1,1], (1,1)))


if __name__ == "__main__":

    unittest.main()