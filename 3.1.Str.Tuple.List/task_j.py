# -*- coding: cp1251 -*-

msg: str = ""
line_msg: str = ""
lst: list = []

while True:
    msg = input()

    if msg == 'ФИНИШ':
        break

    line_msg += msg.lower().strip()

lst = list(line_msg)

lst.sort()

max_quan: int = 1
max_char: str = ""

for item in lst:

    if item == ' ':
        continue

    quan: int = lst.count(item)

    if quan > max_quan:
        max_quan = quan
        max_char = item

print(max_char)
