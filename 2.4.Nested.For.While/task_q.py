m: int = int(input())
count_n: int = 0

for i in range(m):
    n: int = int(input())

    tmp: int = n
    last: int = 0

    while (tmp > 0):
        rem: int = tmp % 10
        tmp //= 10
        last += rem

        if tmp != 0:
            last *= 10

    if last == n:
        count_n += 1

print(f"{count_n}")
