# -*- coding: cp1251 -*-

msg: str = "-"
lst_tmp: list = []
out_lst: list = []

while True:
    msg = input()

    if len(msg) == 0:
        break

    lst_tmp = msg.split("#")
    line: str = lst_tmp[0]
    
    if len(line) == 0:
        continue

    out_lst.append(line)

for _, s in enumerate(out_lst):
    print(s)