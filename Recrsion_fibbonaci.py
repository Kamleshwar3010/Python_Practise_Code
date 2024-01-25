def fibbonaci(l, c, N):
    print(l, end=" ")
    n = c+l
    if N > 0:
        return fibbonaci(c, n, N-1)


val = int(input("Enter The Value- "))
fibbonaci(0, 1, val)
