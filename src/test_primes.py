import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully dtermined to be prime?"""
        self.assertTrue(is_prime(5))
    
    def test_is_1_prime(self):
        """Is five successfully dtermined to be prime?"""
        self.assertTrue(is_prime(10))

if __name__ == '__main__':
    unittest.main()