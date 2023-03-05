class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        lst=[]
        c=""
        for i in range(len(s)):
            if c and c[-1]!=s[i]:
                if len(c)>=3:
                    lst.append([i-len(c),i-1])
                c=s[i]
            else:
                c+=s[i]
        if len(c)>=3:
            lst.append([len(s)-len(c),len(s)-1])
        return lst
