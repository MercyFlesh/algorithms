import unittest
import matplotlib
import random
import time
import matplotlib.pyplot as plt
from timsort import Timsort


class timsortTest(unittest.TestCase):
    #test time sorting an array of n elements
    def test_time_froze(self):
        data = []
        count = 10000
        for _ in range(count):
            data.append(random.randint(0, 30000))

        start_time = time.perf_counter()
        Timsort(data)
        print(f"time froze sort {count} elements: {time.perf_counter() - start_time} sec.\n")

    
    #Checking the sorting of arrays in which there are less than 64 elements
    def test_arr_less_64symb(self):
       
       test_cases = (([8, 1, 7, 4, 0], [0, 1, 4, 7, 8]), ([], []))
       
       for ex, tr in test_cases:
            with self.subTest(n=ex):
                self.assertEqual(Timsort(ex), tr)

    #array sorting test greater than 64
    def test_greater64(self):
        data = []
        for _ in range(100):
             data.append(random.randint(0, 10000))
        Timsort(data)
        for i in range(len(data) - 1):
            with self.subTest(value_1=data[i], value_2=data[i+1]):
                self.assertTrue(data[i] <= data[i + 1])


    
        
if __name__ == "__main__":
    unittest.main()
