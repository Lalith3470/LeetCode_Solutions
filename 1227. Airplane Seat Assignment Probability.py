class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n>=2:
            return 1/2
        else:
            return 1
