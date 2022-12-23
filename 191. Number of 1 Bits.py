class Solution:
    def hammingWeight(self, n: int) -> int:
        n="{:032b}".format(n)
        a=str(n)
        a=a.strip('0')
        count=0
        for i in a:
            if i=='1':
                count+=1
        return count
