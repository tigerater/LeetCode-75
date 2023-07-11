#For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
#Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        #shortest string to str1
        if len(str1)>len(str2):
            str1,str2 = str2,str1

        #iterate backwards over largest factors of length number
        largest_string = ""
        #y is the length of the string that we're considering
        for y in range(len(str1), 0 , -1):
            #if y is divisible into both length of str1 and str2
            if len(str1)/y == int(len(str1)/y) and len(str2)/y == int(len(str2)/y):
                #if the concatenated version of the strings adds up to make both whole strings
                if (len(str1)/y)*str1[:y] == str1 and (len(str2)/y)*str1[:y] == str2:
                    largest_string = str1[:y]
                    return largest_string
        return largest_string
