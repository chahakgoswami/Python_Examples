
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output =[-1 for i in range(2)]
        map = {}
        for i in range(0,len(nums)):
            if nums[i] in map.keys():
                output[0] = i
                output[1] = map[nums[i]]
            else:
                map[target -nums[i]] =  i

        return output



nums = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(nums,target))