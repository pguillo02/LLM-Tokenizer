import utils
import unittest

class test_utils(unittest.TestCase):
    def test_most_common_pair(self):
        self.assertEqual(utils.most_common_pair([1,2,3,4,1,2]), {(1,2):2, (2,3):1, (3,4):1, (4,1):1})
        self.assertEqual(utils.most_common_pair([1,2,1,1,1,1,1,1]), {(1,2):1, (2,1):1, (1,1):5})
        self.assertEqual(utils.most_common_pair([]), ())
        self.assertEqual(utils.most_common_pair([1]), ())
        self.assertEqual(utils.most_common_pair([1,2]), {(1,2):1})
        self.assertEqual(utils.most_common_pair([1,2,3,4,5]), {(1,2):1, (2,3):1, (3,4):1, (4,5):1})

    def test_swapping_most_common_pair(self):
        self.assertEqual(utils.swapping_most_common_pair([1,2,3,4,1,2], (1,2), 5), [5,3,4,5])
        self.assertEqual(utils.swapping_most_common_pair([1,2,1,1,1,1,1,1,1], (1,1), 3), [1,2,3,3,3,1])
        self.assertEqual(utils.swapping_most_common_pair([1,2,3,4,5], (), 6), [1,2,3,4,5])
        self.assertEqual(utils.swapping_most_common_pair([1], (), 1), [1])
        self.assertEqual(utils.swapping_most_common_pair([], (), 1), [])

    def test_training(self):
        self.assertEqual(utils.training_tokenizer([1,2,3,4,1,2], 2), [((1,2), 256)])
        self.assertEqual(utils.training_tokenizer([1,2,1,1,1,1,1,1,1], 3), [((1,1),256),((256,256),257)])
        self.assertEqual(utils.training_tokenizer([1,2,3,4,5], 2), [])
        self.assertEqual(utils.training_tokenizer([1], 1), 0)
        self.assertEqual(utils.training_tokenizer([], 1), 0)

if __name__ == "__main__":

    unittest.main()