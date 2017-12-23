import unittest

from general.json_loader import json_loader


class testJsonLoader(unittest.TestCase):
    """Contains the test for json_loader.
    """

    def test_json_loader(self):
        self.assertIsNotNone(json_loader("tests/sample.json"))
