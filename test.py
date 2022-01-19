import unittest
import time

class PerformanceTestIsOdd(unittest.TestCase):

    def is_odd(self, n):
        return n % 2 == 1

    def test_perf(self):
        start_time = time.time()
        for i in range(1000000):
            self.is_odd(7)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"The test took {elapsed_time} seconds")

if __name__ == "__main__":
    unittest.main()
