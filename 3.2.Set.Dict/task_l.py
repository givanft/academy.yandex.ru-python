n: int = int(input())

surname: dict = {}

while (n > 0):

    person: str = input()

    if surname.get(person) is None:
        surname[person] = 1
    else:
        surname[person] += 1

    n -= 1

namesake: bool = False
for i in sorted(surname):
    if surname[i] >= 2:
        print(f"{i} - {surname[i]}")
        namesake = True

if namesake is False:
    print("Однофамильцев нет")
