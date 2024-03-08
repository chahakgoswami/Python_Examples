from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastgoodindex = len(nums) -1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= lastgoodindex :
                lastgoodindex =i
        return lastgoodindex == 0

sol = Solution()
nums = [2,3,1,1,4]
print(sol.canJump(nums))