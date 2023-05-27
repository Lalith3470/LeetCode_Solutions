class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lst=nums[:]
        self.values=nums[:]

    def reset(self):
        """
        :rtype: List[int]
        """
        self.lst=self.values
        return self.lst

    def shuffle(self):
        """
        :rtype: List[int]
        """
        val=self.lst[:]
        for i in range(len(self.lst)):
            ram=random.randint(i,len(self.lst)-1)
            val[i],val[ram]=val[ram],val[i]
        return val
