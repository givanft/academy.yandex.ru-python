# -*- coding: cp1251 -*-

msg: str = input().lower().strip()
n, m = msg.split()
print(f"{int(n) + int(m)}")
