import unittest

from text_utils import compact


class CompactTests(unittest.TestCase):
    def test_mixed_whitespace(self):
        self.assertEqual(compact(' \talpha  \t beta\n\r\ngamma\t '), 'alpha beta gamma')

    def test_empty_and_whitespace_only(self):
        for text in ('', ' ', '\t\n\r\v\f', ' \t\n  '):
            with self.subTest(text=text):
                self.assertEqual(compact(text), '')

    def test_unicode_whitespace(self):
        self.assertEqual(compact('\u2003alpha\u00a0\u2009beta\u2028'), 'alpha beta')
        self.assertEqual(compact('\u00a0\u2003\u2028'), '')

    def test_preserves_non_whitespace_text(self):
        for text in ('hello', 'Hello, world!', 'café 日本語', 'a_b-c.123'):
            with self.subTest(text=text):
                self.assertEqual(compact(text), text)


if __name__ == '__main__':
    unittest.main()
