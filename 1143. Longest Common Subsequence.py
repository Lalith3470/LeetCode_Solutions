class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cnt=0
        s=0
        for i in range(len(text2)):
            for j in range(len(text2)):
                if text1[i]==text2[j]:
                    cnt+=1
        return cnt
