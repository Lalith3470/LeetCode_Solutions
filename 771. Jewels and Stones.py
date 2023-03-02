class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a=0
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if jewels[j] == stones[i]:
                    a+=1
        return a
