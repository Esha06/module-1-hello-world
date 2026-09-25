import unittest

from hello import greet


class TestGreeting(unittest.TestCase):
    def test_world(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_another_name(self):
        self.assertEqual(greet("Colab"), "Hello, Colab!")


if __name__ == "__main__":
    unittest.main()
