class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        for x in nums:
            if(nums.count(x)==1):
                return x

        