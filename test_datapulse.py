# test_datapulse.py
"""
Tests for DataPulse module.
"""

import unittest
from datapulse import DataPulse

class TestDataPulse(unittest.TestCase):
    """Test cases for DataPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataPulse()
        self.assertIsInstance(instance, DataPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
