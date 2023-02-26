class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        cnt=0
        if len(bits)==1:
            return True
        for i in range(len(bits)):
            if bits[cnt]==1:
                cnt+=2
            else:
                cnt+=1
            if cnt>=len(bits)-1:
                break
        return cnt==len(bits)-1
