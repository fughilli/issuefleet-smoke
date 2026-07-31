"""Tests for the hello-world greeting."""

import unittest

from hello import greeting


class GreetingTest(unittest.TestCase):
    def test_default(self):
        self.assertEqual(greeting(), "Hello, world!")

    def test_named(self):
        self.assertEqual(greeting("Fleet"), "Hello, Fleet!")


if __name__ == "__main__":
    unittest.main()
