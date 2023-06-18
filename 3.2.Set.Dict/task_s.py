n: int = int(input())

toy_dict = {}
while (n > 0):

    _, toy = input().split(":")

    toy_lst: list = toy.split(",")

    for item in toy_lst:
        item = item.strip()
        if toy_dict.get(item) is None:
            toy_dict[item] = 1
        else:
            toy_dict[item] += 1

    n -= 1

toys_lst: list = []

for key, value in toy_dict.items():
    if value == 1:
        toys_lst.append(key)

for item in sorted(toys_lst):
    print(item)