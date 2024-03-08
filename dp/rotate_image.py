from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)

        for i in range(0,row):
            for j in range(i,row):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(0,row):
            for j in range(0,row//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][row-1-j]
                matrix[i][row-1-j] = temp


matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
sol.rotate(matrix)
print(matrix)