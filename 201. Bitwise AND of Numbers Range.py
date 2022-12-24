class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right&(right-1)>left:  
            right=right&(right-1)
        return left&right
