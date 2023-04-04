class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        tmp=[0]*(n+1)
        for i in bookings:
            tmp[i[0]-1]+=i[2]
            tmp[i[1]]-=i[2]
        sm=0
        for i in range(n):
            tmp[i]+=sm
            sm=tmp[i]
        return tmp[:n]
