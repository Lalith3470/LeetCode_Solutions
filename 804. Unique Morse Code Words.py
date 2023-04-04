class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic={"a":".-","b":"-...","c":"-.-.",
            "d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..",
            "j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---",
            "p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-",
            "w":".--","x":"-..-","y":"-.--","z":"--.."}
        cnt=[]
        for i in words:
            s=""
            for j in i:
               s+=dic[j]
            if s not in cnt:
                cnt.append(s)
        return len(cnt)
