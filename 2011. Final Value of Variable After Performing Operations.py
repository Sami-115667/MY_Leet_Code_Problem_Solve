class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        c=0
        for x in operations:
            if "-" in x:
                c=c-1
            else:
                c=c+1
        return c