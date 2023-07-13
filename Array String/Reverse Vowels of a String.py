#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_pos = []
        vowels = ["a","e","i","o","u","A","E","I","O","U"]

        return_string = []
        for v in s:
            return_string+=v

        #iterate over and collect the position of the vowels
        for x in range(len(s)):
            if s[x] in vowels:
                vowel_pos.append(x)
        
        #reverse positions and rebuild string
        for y in range(len(vowel_pos)):
            return_string[vowel_pos[y]] = s[vowel_pos[-y-1]]
        
        return "".join(return_string)
