class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bans="bans"
        ol="ol"
        lst=[]
        dict=Counter(text)
        for i,j in dict.items():
            if i in bans:
                lst.append(j)
            elif i in ol:
                lst.append(int(j/2))
        if len(lst)>=5:
            return min(lst)
        else:
            return 0
