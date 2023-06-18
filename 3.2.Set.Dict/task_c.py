n: int = int(input())

org_lst: list = []
while (n > 0):
    lst: list = list(input().split())
    org_lst.extend(lst)       
    n -= 1

for i in set(org_lst):
    print(i)