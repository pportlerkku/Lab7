import unittest
from source.CountClump import CountClump

class TestCountClumps(unittest.TestCase):

    def test_TC1(self):
        self.assertEqual(CountClump.count_clumps([]), 0)

    def test_TC2(self):
        self.assertEqual(CountClump.count_clumps([1]), 0)

    def test_TC3(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 3, 4, 5]), 0)

    def test_TC4(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 1, 1, 1]), 1)

    def test_TC5(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 2, 3, 3, 4, 4, 4, 1]), 3) 

    def test_TC6(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 2, 2, 3, 3, 3]), 3)  

if __name__ == "__main__":
    unittest.main()
