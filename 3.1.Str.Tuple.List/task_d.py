# -*- coding: cp1251 -*-

msg: str = "-"
lst: list = list()

while True:
    msg = input()

    if len(msg.strip()) == 0:
        break

    if msg.endswith("@@@"):
        continue

    if msg.startswith("##"):
        msg = msg[2:]

    lst.append(msg)

for _, s in enumerate(lst):
    print(s)
