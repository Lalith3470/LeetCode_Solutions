class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:return s
        lst=['']*numRows
        cnt=0
        val=-1
        for i in s:
            lst[cnt]+=i
            if cnt==0 or cnt==numRows-1:
                val*=-1
            cnt+=val
        return "".join(lst)
