def deli(a):
    d = 2
    k = 0
    while d * d < a:
        if a % d == 0:
            if d % 2 == 0:
                k += 1
            if (a // d) % 2 == 0:
                k += 1
        d += 1
    if d * d == a and d % 2 == 0:
        k += 1
    return k

maxd = 0
ch = 0
for i in range(595960, 669119 + 1):
    res = deli(i)
    if maxd < res:
        maxd = res
        ch = i
print(maxd)

k = 0
for i in range(ch - 1, 2, -1):
    if ch % i == 0:
        print(i, end=' ')
        k += 1
    if k >= 2:
        break
