#There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

#Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

#Note that multiple kids can have the greatest number of candies.

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        #make a second array of candies with the potential max values for each kid
        candies_potential = [0]*len(candies)
        for x in range(len(candies)):
            candies_potential[x] = candies[x]+extraCandies

        #return array
        answer_array = []

        test = max(candies)
        #for each value, check if it'll be bigger than or equal to anything in the original array
        for x in candies_potential:
            if x>=test:
                answer_array.append(True)
            else:
                answer_array.append(False)
            
        return answer_array
