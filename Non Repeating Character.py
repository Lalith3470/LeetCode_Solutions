
from collections import Counter
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        cnt=Counter(s)
        for i in s:
            if cnt[i]==1:return i
        return "$"
