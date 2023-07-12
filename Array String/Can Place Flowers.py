#You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        #We'll iterate through the list, adding flowers as we go.
        #If there are 0 flowers to add, it's always true
        if n==0:
            return True
        #If the flowerbed is 0, it'll return true as it dictates that n will be under max length
        if flowerbed == [0]:
            return True

        
        if len(flowerbed)>1:
            #edge cases at the front and back
            if flowerbed[0] == 0 and flowerbed [1] == 0:
                flowerbed [0] = 1
                n-=1
            if flowerbed[-1] == 0 and flowerbed [-2] == 0:
                flowerbed [-1] = 1
                n-=1
            #no more flowers to add
            if n <=0:
                    return True

            #iterate through, looking one and two ahead
            for x in range(len(flowerbed)-2):
                if n <=0:
                    return True
                if  flowerbed[x]==0 and flowerbed[x+1]==0 and flowerbed[x+2]==0:
                    flowerbed[x+1]=1
                    n-=1
                
        return False
