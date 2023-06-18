n: int = int(input())

sad: dict = {}
find_by: str = ""
while (n > -1):
    child_lst: list = input().split()
    if len(child_lst) == 1:
        find_by = child_lst[0]
        break
    child = child_lst[0]
    for item in child_lst:
        if child == item:
            continue        
        if sad.get(item) is None:
            sad[item] = [child]
        else:
            sad[item] += [child]
    n -= 1

fb = sad.get(find_by)
if fb is None:
    print("Таких нет")
else:
    fb.sort()
    for item in fb:
        print(f"{item}")