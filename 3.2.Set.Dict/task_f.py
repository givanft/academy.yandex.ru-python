n: int = int(input())
m: int = int(input())

gr1: set = set()
gr2: set = set()

nm: int = n + m
while (nm > 0):
    child: str = input()
    if child in gr1:
        gr2.add(child)
    else:
        gr1.add(child)
    
    nm -= 1

diff: set = gr1 - gr2
if len(diff) == 0:
    print("Таких нет")
else:
    for child in sorted(diff):
        print(f"{child}")
