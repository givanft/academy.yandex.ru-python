# -*- coding: cp1251 -*-

n: int = int(input())
quan: int = 0

for _ in range(n):
    msg: str = input().lower().strip()
    lst: list = msg.split()
    quan += lst.count("зайка")

print(f"{quan}")