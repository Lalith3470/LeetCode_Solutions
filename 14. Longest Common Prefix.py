class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s=""
        for i in zip(*strs):
            if len(set(i))==1:
                s+=i[0]
            else:
                break
        return s
