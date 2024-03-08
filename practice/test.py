from numpy import *


def arr_example():
    arr = array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j])


def var_example(a):
    print("a id =", id(a))
    a[1] = 10
    print("a id =", id(a))
    print("a =", a)


x = array([1, 2, 3, 4, 5])

result = list(filter(lambda a: a % 2 == 0, x))

print(result)
