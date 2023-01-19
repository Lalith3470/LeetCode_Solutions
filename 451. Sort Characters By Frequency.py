class Solution:
    def frequencySort(self, s: str) -> str:
        freq={ }
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        res=""
        for i in sorted(freq, key=freq.get, reverse=True):
            res+=i*freq[i]
        return res
