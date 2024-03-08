from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        column = len(matrix[0])
        left = 0
        right = column-1
        top = 0
        buttom = row-1
        div =0
        output =[]
        while (left <= right and top <= buttom):

            if (div ==0):
                for i in range(left,right+1,1):
                    output.append(matrix[top][i])
                top +=1
            elif (div ==1):
                for i in range(top,buttom+1,1):
                    output.append(matrix[i][right])
                right -=1
            elif (div==2):
                for i in range(right,left-1,-1):
                    output.append(matrix[buttom][i])
                buttom -=1
            elif (div ==3):
                for i in range(buttom,top-1,-1):
                    output.append(matrix[i][left])
                left+=1
            div = (div+1)%4
        return output

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.spiralOrder(matrix))