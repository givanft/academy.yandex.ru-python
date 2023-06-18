n: int = int(input())
m: int = int(input())

child_n: set = set()
while (n > 0):
    child_n.add(input())
    n -= 1

child_m: set = set()
while (m > 0):
    child_m.add(input())
    m -= 1

k: int = len(child_n ^ child_m)
if k == 0:
    print("Таких нет")    
else:
    print(f"{k}")
