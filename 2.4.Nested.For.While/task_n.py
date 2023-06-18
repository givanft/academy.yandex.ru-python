# -*- coding: cp1251 -*-

n: int = int(input())
m: int = int(input())

num: int = n * m
tmp: int = num

len_num: int = 0
while (tmp > 0):
    tmp //= 10
    len_num += 1

c: int = 0
reverse: int = 1

while (c < num):
    
    a: int = c + 1
    b: int = a + m

    if reverse == -1:
        tmp = a - 1
        a = b - 1
        b = tmp

    for i in range(a, b, reverse):
         print(f"{str(i).rjust(len_num, ' ')} ", end="")
         c += 1

    reverse *= -1
    print()
