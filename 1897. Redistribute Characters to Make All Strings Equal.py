class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        ln=len(words)
        cnt=Counter("".join(words))
        for i in cnt.values():
            if i%ln!=0:return False
        return True
