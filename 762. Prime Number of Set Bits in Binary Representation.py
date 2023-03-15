class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prime_list=[2,3,5,7,11,13,17,19]
        c=0
        while left<=right:
            cnt=bin(left).count("1")
            if cnt in prime_list:c+=1
            left+=1
        return c
