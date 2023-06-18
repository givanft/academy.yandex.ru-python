# -*- coding: cp1251 -*-

n: int = int(input())
lst_in: list = []
search_by: str = ""

n += 1
while (n != 0):
    if n != 1:
        lst_in.append(input())
    else:
        search_by = input()
    n -= 1

for item in lst_in:
    if search_by.lower() in item.lower():
        print(item)
