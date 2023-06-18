# -*- coding: cp1251 -*-

n: int = int(input())
lst_n: list = []
power: int = 1

n += 1
while ((n := n - 1) > -1):
    if n == 0:
        power = int(input())
    else:
        lst_n.append(int(input()))

for i in range(len(lst_n)):
    print(f"{lst_n[i] ** power}")