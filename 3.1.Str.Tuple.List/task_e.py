# -*- coding: cp1251 -*-

msg: str = input().lower().strip()
out: bool = "YES"

for i in range(len(msg) // 2):
    if msg[i] != msg[-(i + 1)]:
        out = "NO"
        break

print(out)