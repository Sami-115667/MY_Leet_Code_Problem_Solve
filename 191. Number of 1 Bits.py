class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=0
        while n>0:
            if n%2==0:
                n=n/2
            else:
                result=result+1
                n=n-1
                n=n/2
        return result