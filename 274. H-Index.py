class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations=citations[::-1]
        for i in range(len(citations)):
            #print(i, citations[i])
            if citations[i]<=i:
                return i
        return len(citations)     
