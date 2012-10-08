import unittest

import solution01
import solution02

class BaseAnagramTestCase(unittest.TestCase):
    anagram_class = None

    def setUp(self):
        self.str1 = "This is an anagram test"
        self.str1_shuffle = "test This an is  anagram"
        self.str1_nospace = "anagramThisistestan"
        self.str1_camelcase = "Test This An Anagram Is"
        self.str2 = "This is not"

    def test_same_string(self):
        self.assertTrue(self.anagram_class.is_anagram(self.str1, self.str1))

    def test_shuffle_string(self):
        self.assertTrue(self.anagram_class.is_anagram(self.str1,
                                                      self.str1_shuffle))

    def test_nospace_string(self):
        self.assertTrue(self.anagram_class.is_anagram(self.str1,
                                                      self.str1_nospace))

    def test_different_case_string(self):
        self.assertTrue(self.anagram_class.is_anagram(self.str1,
                                                      self.str1_camelcase))

    def test_not_anagram(self):
        self.assertFalse(self.anagram_class.is_anagram(self.str1,
                                                       self.str2))


class Solution01TestCase(BaseAnagramTestCase):
    anagram_class = solution01.Anagram


class Solution02TestCase(BaseAnagramTestCase):
    anagram_class = solution02.Anagram

if __name__ == '__main__':
    print "Testing solution01..."
    suite = unittest.TestLoader().loadTestsFromTestCase(Solution01TestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print "Testing solution02..."
    suite = unittest.TestLoader().loadTestsFromTestCase(Solution02TestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)