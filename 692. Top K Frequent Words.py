class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        s = sorted(words) 
        c = Counter(s) 
        return [word for word, i in c.most_common(k)]
