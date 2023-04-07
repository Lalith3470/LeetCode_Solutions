class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=Counter(chars)
        cnt=0
        for i in words:
            ch_cnt=Counter(i)
            ct=0
            for chr,freq in ch_cnt.items():
                if chr in c:
                    if freq<=c[chr]:
                        ct+=freq
            if ct==len(i):
                cnt+=ct
        return cnt
