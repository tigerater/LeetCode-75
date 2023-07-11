#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        #The merged string that we'll be adding to.
        merged_string = ""

        #iterate over the max length of either word
        for x in range(max(len(word1),len(word2))):
            #if the current x isn't outside the range of the word
            if x<len(word1):
                #add the letter onto the merged word.
                merged_string+=word1[x]
            if x<len(word2):
                merged_string+=word2[x]
        return merged_string
