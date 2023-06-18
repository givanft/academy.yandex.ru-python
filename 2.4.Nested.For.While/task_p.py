# -*- coding: cp1251 -*-

n: int = int(input())
m: int = int(input())

prod: int = n * n
len_prod: int = len(str(prod))

if len_prod > m:
    m = len_prod

for i in range(1, n + 1):
    for j in range(1, n + 1):

        prod = i * j # 16
        len_num: int = len(str(prod)) # 2

        rr: int = 0
        ll: int = 0

        if m > len_num:
            dx = m - len_num # 3 - 2 = 1
            rr = dx // 2
            ll = dx - rr

        print(f"{' '}" * rr, end="")
        print(f"{prod}", end="")
        print(f"{' '}" * ll, end="")
        if j != n:
            print("|", end="")

    print()
    if i != n:
        s: str = ("-".center(m, '-') + "-") * n
        print(s[:-1])

