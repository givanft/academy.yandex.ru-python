# -*- coding: cp1251 -*-

n: int = int(input())

line_n: int = 0
s_min: str = ""
s_current: str = ""

while (line_n < n):
    line_n += 1
    s_current += str(line_n)
    
    if len(s_current) > len(s_min):
        s_min = s_current
        s_current = ''
        continue

    s_current += ' '

len_num: int = len(s_min)

line_n: int = 0
s_min: str = ""
s_current: str = ""

while (line_n < n):
    line_n += 1
    s_current += str(line_n)
    
    if len(s_current) > len(s_min):
        s_min = s_current
        dx = len_num - len(s_min)
        r = dx // 2
        l = dx - r
        print(f"{' '}" * r, end = "")
        print(f"{s_min}", end = "")
        print(f"{' '}" * l, end = "")
        print()
        s_current = ''
        continue

    s_current += ' '
