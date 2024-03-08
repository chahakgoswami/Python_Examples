class Solution:
    def minDistance(self, word1: str, word2: str) -> int: 
        row = len(word1)
        col = len(word2)
        dp = [[0 for i in range(col+1)] for j in range(row+1)]

        for i in range(0,row+1):
            for j in range(0,col+1):
                if i ==0:
                    dp[i][j] = j
                elif j==0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else :
                    dp[i][j] = 1+ min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])

        return dp[row][col]


word1 = "horse"
word2 = "ros"
sol = Solution()
print(sol.minDistance(word1,word2))