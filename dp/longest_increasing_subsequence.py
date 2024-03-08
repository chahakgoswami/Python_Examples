from typing import List
import numpy as np
import sys
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = np.arange(length)
        dp.fill(1)

        for i in range(1,length,1):
            for j in range(0,i,1):
                if ( nums[i] > nums[j] and 
                     dp[i] <= dp[j]
                   ):
                    dp[i] = dp[j] +1 
        
        max_size = -sys.maxsize - 1
        for val in dp:
            max_size = max(max_size,val)

        return max_size

sol = Solution()
nums = [1, 101, 2, 3, 100]
ans = sol.lengthOfLIS(nums)
print(ans)
