n: int = int(input())

total_dish: dict = {}

while (n > 0):
    dish: str = input()
    total_dish[dish] = 0
    n -= 1

days: int = int(input())

while (days > 0):

    n_dish: int = int(input())

    while (n_dish > 0):

        dish = input()
        total_dish[dish] += 1
        n_dish -= 1
    
    days -= 1

todo: bool = False
for i in sorted(total_dish):
    if total_dish[i] == 0:
        print(f"{i}")
        todo = True

if todo is False:
    print("Готовить нечего")
