class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        cnt=1
        nums=[*set(nums)]
        nums.sort()
        mx=0
        #print(nums)
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                cnt+=1
            else:
                mx=max(cnt,mx)
                cnt=1
        return max(mx,cnt)

    
