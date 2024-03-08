import numpy as np
import sys
class Solution:
    def maxSumIS(self, Arr, n):
        dp = np.arange(n)
        for i in range(0,n,1):
            dp[i] = Arr[i]

        for  i in range(1,n,1):
            for  j in range(0,i,1):
                if (
                    Arr[i] > Arr[j] and
                    dp[i] < dp[j] + Arr[i]
                    ):
                    dp[i] = dp[j] + Arr[i]
        
        max_val = -sys.maxsize -1

        for val in dp:
           max_val = max(max_val,val)
        
        return max_val

sol = Solution()
nums = [1, 101, 2, 3, 100, 4, 5]
ans = sol.maxSumIS(nums,len(nums))
print(ans)