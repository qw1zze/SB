def deli(a):
    k = 0
    d = 2
    d1 = 0
    d2 = 0
    while a > d * d:
        if a % d == 0:
            k += 2
            if d1 == 0:
                d1 = d
                d2 = a // d
        d += 1
    if d * d == a:
        k += 1
    if k == 7:
        return d1, d2
    return 0

for i in range(706070, 726396 + 1):
    res = deli(i)
    if res != 0:
        print(res[0], res[1])
