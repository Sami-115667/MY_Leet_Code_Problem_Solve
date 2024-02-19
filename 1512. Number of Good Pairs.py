class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=0
        nums1=set(nums)
        for x in nums1:
            if x in nums:
                y=nums.count(x)
                y=y-1
                z=((y+1)*y)/2
                r=r+z
        return r
        