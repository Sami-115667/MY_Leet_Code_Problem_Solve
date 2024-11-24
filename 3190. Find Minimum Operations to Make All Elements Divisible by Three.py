class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for num in nums:
            if(num%3!=0):
                total=total+1
        return total

        