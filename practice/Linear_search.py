

def search(list, num):
    pos = 1
    for i in range(len(list)):
        if list[i] == num:
            return i
    return -1


list = [1, 5, 3, 4, 7, 6, 9, 19]
num = 10

ind = search(list, num)
if ind != -1:
    print("FOUND AT INDEX = ", ind)
else:
    print("NOT FOUND")
