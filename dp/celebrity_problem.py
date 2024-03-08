class Solution:

    def celebrity(self, M):
        candidate =0
        for i in range(0,len(M)):
            if M[candidate][i] ==1:
                candidate = i
            
        
        for i in range(0,len(M)):
            if i != candidate and ( M[i][candidate] ==0 or M[candidate][i] ==1):
                return -1
        return candidate

M= [[0, 1, 0],[0 ,0, 0],[0 ,1 ,0]]
sol = Solution()
print(sol.celebrity(M))
