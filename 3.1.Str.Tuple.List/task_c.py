# -*- coding: cp1251 -*-

l: int = 10#int(input())
n: int = 2#int(input())

for i in range(n):

    msg: str = input()
    suff: str = ""

    if len(msg) > l:
        msg = msg[:(l - 3)]
        suff = "..."

    print(f"{msg}{suff}")