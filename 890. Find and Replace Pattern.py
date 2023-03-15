class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[list]:
        lst=[]
        for i in words:
            if len(set(zip(pattern,i)))==len(set(i))==len(set(pattern)):
                lst.append(i)
        return lst
                                                                            

                          
