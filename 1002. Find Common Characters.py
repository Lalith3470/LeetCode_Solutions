class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cmn=Counter(words[0])
        lst=[]
        
        for word in range(1,len(words)):
            cmn=cmn & Counter(words[word])
        for i,j in cmn.items():
            for res in range(j):
                lst.append(i)
        return lst
