import unittest
from hello import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_three_prime(self):
        """Is five successfully dtermined to be prime?"""
        self.assertTrue(is_prime(3))
    
    
    def test_is_four_prime(self):
        """Is five successfully dtermined to be prime?"""
        self.assertFalse(is_prime(4))
    
    
if __name__ == '__main__':
    unittest.main()