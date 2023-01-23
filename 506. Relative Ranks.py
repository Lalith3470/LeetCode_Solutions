class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l = []
        M= {0:"Gold Medal", 1:"Silver Medal", 2:"Bronze Medal"}
        s = sorted(score, reverse=True)
        for i in score:
            a = s.index(i)
            if a in [0, 1, 2]:
                l.append(M[a])
            else:
                l.append(str(a + 1))
        return l
