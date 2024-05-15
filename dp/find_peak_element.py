def find_peak_element(nums):
    l = 0
    h = len(nums) - 1
    
    while l <= h:
        m = l + (h - l) // 2
        
        if m + 1 < len(nums) and nums[m] <= nums[m + 1]:
            l = m + 1
        else:
            h = m - 1
    
    return l
