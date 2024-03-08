from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = height[0]
        right_max = height[len(height)-1] 
        left =0
        right = len(height)-1
        area = 0
        while left <= right:
            if left_max < right_max :
                if  height[left] > left_max:
                    left_max = height[left]
                else:
                    area += (left_max - height[left])
                left+=1
            else:
                if  height[right] > right_max:
                    right_max = height[right]
                else:
                    area += (right_max - height[right])
                right-=1
        return area

            
sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol.trap(height)