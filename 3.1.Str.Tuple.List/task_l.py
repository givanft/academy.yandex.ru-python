# -*- coding: cp1251 -*-

kasha: list = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
n: int = int(input())

len_kasha: int = len(kasha)
m: int = n // len_kasha
rem: int = n % len_kasha

for i in range(m):
    for j in range(len_kasha):
        print(kasha[j])

for i in range(rem):
    print(kasha[i])
