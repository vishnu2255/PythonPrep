def fun() -> object:
    global x
    y = 2 + x[0]
    print(y)
    x[0] = 90


x = [1, 2, 3]
fun()


a = 12
a = 13

print(a)
