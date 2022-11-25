s=nums1+nums2
s.sort()
if len(s)%2==0:
    ln = int(len(s)/2)
    median = s[ln]+s[ln-1]
    return float(median/2)
else:
    return float(s[int(len(s)/2)])
