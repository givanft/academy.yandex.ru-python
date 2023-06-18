# -*- coding: cp1251 -*-

nums: str = input()
power: int = int(input())

lst_n: list = nums.split()

for i in range(len(lst_n)):
    print(f"{int(lst_n[i]) ** power}", end=" ")

