# -*- coding: cp1251 -*-

n: int = int(input())
m: int = int(input())

num: int = n * m
tmp: int = num

len_num: int = 0
while (tmp > 0):
    tmp //= 10
    len_num += 1

for i in range(1, n + 1):
    for j in range(i, num + 1, n):
        print(f"{str(j).rjust(len_num, ' ')} ", end="")
    print()
