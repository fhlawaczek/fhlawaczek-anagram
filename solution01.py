class Anagram(object):
    @staticmethod
    def is_anagram(str1, str2):
        """Returns whether strings are anagrams (case and space insensitive)."""
        letter_list1 = list(str1.replace(" ", "").upper())
        letter_list1.sort()
        letter_list2 = list(str2.replace(" ", "").upper())
        letter_list2.sort()
        return (letter_list1 == letter_list2)
