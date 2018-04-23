import pickle
import unittest

from config import path_to_counter

class TestDataMethods(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        with open(path_to_counter, "rb") as f:
            cls.counter = pickle.load(f)

    def test_key_count(self):
        self.assertGreaterEqual(len(self.counter), 1e5)
        
    def test_key_type(self):
        a, b = self.counter.most_common(1)[0][0]
        self.assertEqual(type(a), str)
        self.assertEqual(type(b), str)

if __name__ == '__main__':
    unittest.main()
