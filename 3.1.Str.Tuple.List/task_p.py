# -*- coding: cp1251 -*-

l_total: int = int(input())
n: int = int(input())

lst_msg: list = []

for _ in range(n):
    msg: str = input()
    count_chars: int = len(msg)
    
    if l_total < 3:
        if len(lst_msg) == 0:
            lst_msg.append("...")
        continue

    if count_chars < l_total:
        diff: int = l_total - count_chars
        if 0 <= diff <= 3:
            lst_msg.append(msg[:(count_chars - (3 - diff))] + "...")
        else:
            lst_msg.append(msg)
    else:
        lst_msg.append(msg[:(l_total - 3)] + "...")

    l_total -= count_chars

for item in lst_msg:
    print(item)
