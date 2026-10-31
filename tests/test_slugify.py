import unittest

from src.slugify import slugify


class SlugifyTest(unittest.TestCase):
    def test_lowercases(self):
        self.assertEqual(slugify("Hello"), "hello")

    def test_spaces_become_dashes(self):
        self.assertEqual(slugify("hello world"), "hello-world")

    def test_strips_punctuation(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_collapses_repeated_separators(self):
        self.assertEqual(slugify("a  --  b"), "a-b")

    def test_trims_leading_and_trailing_dashes(self):
        self.assertEqual(slugify("  --Hi there--  "), "hi-there")

    def test_empty_and_symbol_only(self):
        self.assertEqual(slugify(""), "")
        self.assertEqual(slugify("!!!"), "")


if __name__ == "__main__":
    unittest.main()
