#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output_array = []

        total_expansion = 1
        #if there is one 0 in array
        if nums.count(0)==1:
            pos_0 = 0
            #iterate per value to find total multiplication excluding the 0
            for x in range(len(nums)):
                if nums[x]==0:
                    nums[x] = 1
                    pos_0 = x
                #replace 0 with a 1 for total multiplication
                total_expansion=total_expansion*nums[x]
            for y in range(len(nums)):
                if pos_0 == y:
                    #if we're at the 0, multiply the others
                    output_array.append(total_expansion/nums[y])
                else:
                    #if we're not at the 0, the 0 will wipe out the result
                    output_array.append(0)
        else:
            for z in range(len(nums)):
                #calculate total expansion
                total_expansion = total_expansion*nums[z]
            for a in range(len(nums)):
                if nums[a]==0:
                    #can only get here if there are 2 or more 0s
                    output_array.append(0)
                else:
                    output_array.append(total_expansion/nums[a])

        return(output_array)
