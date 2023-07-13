#Given an input string s, reverse the order of the words.

#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

#Return a string of the words in reverse order concatenated by a single space.

#Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        #split words by spaces
        words = s.split()
        return_words = []
        for x in words:
            #insert words at the start of the list- ends up reversed
            return_words.insert(0,x)

        return " ".join(return_words)
