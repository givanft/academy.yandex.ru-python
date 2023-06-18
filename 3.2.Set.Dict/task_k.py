n: int = int(input())

surname: dict = {}

while (n > 0):

    person: str = input()

    if surname.get(person) is None:
        surname[person] = 1
    else:
        surname[person] += 1

    n -= 1

sum: int = 0
for value in surname.values():
    if value >= 2:
        sum += value

print(f"{sum}")