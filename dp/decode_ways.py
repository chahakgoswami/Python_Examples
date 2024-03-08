class Solution:
    def numDecodings(self, s: str) -> int:

        dp =[0 for i in range(len(s)+1)]
        dp[0] =1
        if s[0] == '0':
            dp[1] =0 
        else:
            dp[1] =1

            for i in range(2 , len(s)+1):
                onedigit =  int(s[i-1:i])
                twodigit =  int(s[i-2:i])
                if onedigit >=1:
                    dp[i] = dp[i]+dp[i-1]

                if twodigit > 9 and twodigit <=26 :
                    dp[i] = dp[i]+dp[i-2]

        return dp[len(s)]


sol = Solution()
print(sol.numDecodings("226"))
