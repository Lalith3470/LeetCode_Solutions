class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        s=''
        for i in range(len(num)):
            s+=str(num[i])
        sum = str(k+int(s))
        l=[]
        for i in range(len(sum)):
            l.append(int(sum[i]))
        return l
