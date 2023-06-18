# -*- coding: cp1251 -*-

nums: str = input()
lst_n: list = nums.split()

x = int(lst_n[0])

for i in range(1, len(lst_n)):
    y: int = int(lst_n[i])

    while (x != y):
        if x > y:
            x -= y
        else:
            y -= x

print(f"{x}")
