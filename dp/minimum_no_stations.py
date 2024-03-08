
from typing import List
class Solution:
    def minimumStations(self, arr:List[int] , dept: List[int])->int:
        arr.sort()
        dept.sort()
        i =1
        j =0
        n = len(arr)
        req_platform = 1
        max_platform = 1

        while(i<n and j<n):
            if (arr[i] <= dept[j]):
                req_platform +=1
                if(req_platform > max_platform):
                    max_platform = req_platform
                i+=1
            else:
                req_platform -=1
                j+=1

        return max_platform


sol = Solution()
arr   = [900, 940, 950, 1100, 1500, 1800]; 
dept   = [910, 1200, 1120, 1130, 1900, 2000]; 

print(sol.minimumStations(arr,dept))

