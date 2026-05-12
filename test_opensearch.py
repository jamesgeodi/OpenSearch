# test_opensearch.py
"""
Tests for OpenSearch module.
"""

import unittest
from opensearch import OpenSearch

class TestOpenSearch(unittest.TestCase):
    """Test cases for OpenSearch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OpenSearch()
        self.assertIsInstance(instance, OpenSearch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OpenSearch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
