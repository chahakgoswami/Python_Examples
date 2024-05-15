def min_platform_required(arr, dep):
    arr.sort()
    dep.sort()
    max_platform = 1
    req_platform = 1
    i = 1
    j = 0
    n = len(arr)

    while i < n and j < n:
        if arr[i] < dep[j]:
            i += 1
            req_platform += 1
            max_platform = max(max_platform, req_platform)
        else:
            j += 1
            req_platform -= 1

    return max_platform

# Example usage
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(min_platform_required(arr, dep))
