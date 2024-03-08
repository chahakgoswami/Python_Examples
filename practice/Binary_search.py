

def binary_search(list, num):
    left = 0
    right = len(list)-1

    while (left <= right):
        mid = left + (right-left)//2
        if list[mid] == num:
            return mid
        elif list[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return -1


list = [1,  3, 4, 7,  9, 19, 21]
num = 22
ind = binary_search(list, num)
if ind != -1:
    print("FOUND AT INDEX = ", ind)
else:
    print("NOT FOUND")
