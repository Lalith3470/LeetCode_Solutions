class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        li = []
        for i in range(len(words)):
            wo = words[i]
            first = 0
            second = 0
            third = 0
            for j in range(0,len(wo)):
                if wo[j].lower() in ('q','w','e','r','t','y','u','i','o','p'):
                    first += 1
                elif wo[j].lower() in ('a','s','d','f','g','h','j','k','l'):
                    second+=1
                else:
                    third+=1  
            if len(wo)==first or len(wo)==second or len(wo) == third:
                li.append(wo)
        return li
