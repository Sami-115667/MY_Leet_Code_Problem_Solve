class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        l=""
        for x in address:
            if x==".":
                l=l+"[.]"
            else:
                l=l+x
        return l

        # return address.replace(".", "[.]")