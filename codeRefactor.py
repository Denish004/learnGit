def f(a):
    s = 0
    for i in range(len(a)):
        if a[i] > 0:
            s += a[i]
    return s

x = [10, -5, 20, -3, 15]
print(f(x))