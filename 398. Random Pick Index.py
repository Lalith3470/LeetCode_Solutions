class Solution:

    def __init__(self, nums: List[int]):
        self.dic=defaultdict(list)
        for i in range(len(nums)):
            self.dic[nums[i]].append(i)
    
    def pick(self, target: int) -> int:
        return random.choice(self.dic[target])
