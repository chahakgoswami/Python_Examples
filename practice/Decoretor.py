def div(a, b):
    print(a/b)


def change_div(func):
    def inner(a, b):
        if (a < b):
            a, b = b, a
        return func(a, b)
    return inner


div = change_div(div)
div(2, 4)
