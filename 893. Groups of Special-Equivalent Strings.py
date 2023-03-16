class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lst=[]
        for i in words:
            evn=''
            odd=''
            for j in range(len(i)):
                if j%2==0:
                    evn+=i[j]
                else:
                    odd+=i[j]
            str=sorted(evn)+sorted(odd)
            lst.append("".join(str))
        return len(Counter(lst))
