# -*- coding: cp1251 -*-

n: int = int(input())
msg: str = "YES"

for i in range(n):
    fruit: str = input()
    if fruit.startswith(('�', '�', '�')) is False:
        msg: str = "NO"

print(msg)
