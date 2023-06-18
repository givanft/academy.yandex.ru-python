fauna: dict = {}

while ((forest_item := input()) != ""):
    item_lst: list = forest_item.split()

    for item in item_lst:
        if fauna.get(item) is None:
            fauna[item] = 1
        else:
            fauna[item] += 1

for key, value in fauna.items():
    print(f"{key} {value}")
