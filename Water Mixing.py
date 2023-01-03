class Solution:
    def firstBadVersion(self, n: int) -> int:
        start=0
        end=n
        while start<end:
            mid=(start+end)/2
            if isBadVersion(mid):
                end=mid
            else:
                start=mid+1
        return int(start)
