import csv
import pickle
import unittest

from config import path_to_counter, path_to_tsv

class TestDataMethods(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        with open(path_to_counter, "rb") as f:
            cls.counter = pickle.load(f)
        
        lines = []
        with open(path_to_tsv, "r") as f:
            line_count = 1000
            for line in csv.DictReader(f, delimiter="\t"):
                lines.append(line)
        cls.lines = lines

    def test_key_count(self):
        self.assertGreaterEqual(len(self.counter), 1e5)
        
    def test_key_type(self):
        a, b = self.counter.most_common(1)[0][0]
        self.assertEqual(type(a), str)
        self.assertEqual(type(b), str)
        
    def test_lines(self):
        line = self.lines[0]
        self.assertEqual(type(line["a"]), str)
        self.assertEqual(type(line["b"]), str)
        self.assertEqual(type(int(line["count"])), int)        

if __name__ == '__main__':
    unittest.main()
