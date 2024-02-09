class Solution(object):
    def addBinary(self, a, b):
       
       a=int(a,2)
       b=int (b,2)
       a=a+b
       return bin(a)[2:]
        