"""Unit Test: sample"""
import unittest

from pyspark.sql import SparkSession
from parfum.sample import sample_helloworld

class TestSample(unittest.TestCase):
    """Test Case: sample"""

    def test_001(self):
        """Test Case 001"""
        spark = SparkSession.builder.appName("sample_test001").getOrCreate()
        sample_helloworld.run(spark)

if __name__ == "__main__":
    unittest.main()
