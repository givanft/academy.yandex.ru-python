# -*- coding: cp1251 -*-

n: int = int(input())
pattern: str = "зайка"
out_lst: list = []

for _ in range(n):
    msg: str = input().lower().strip()
    lst: list = msg.split()

    quan: int = 0
    out: str = "Заек нет =("

    for item in lst:
        if item != pattern:
            quan += len(item)
        else:
            quan += 1
            out = str(quan)
            break
        quan += 1

    out_lst.append(out)

for _, s in enumerate(out_lst):
    print(f"{s}")