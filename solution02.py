class Anagram(object):
    @staticmethod
    def is_anagram(str1, str2):
        """Returns whether strings are anagrams (case and space insensitive)."""
        str1_histo = {}
        str2_histo = {}
        for l in str1.replace(" ", "").upper():
            str1_histo[l] = str1_histo.get(l, 0) + 1
        for l in str2.replace(" ", "").upper():
            str2_histo[l] = str2_histo.get(l, 0) + 1
        return str1_histo == str2_histo