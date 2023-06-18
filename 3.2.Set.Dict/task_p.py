
near_bunny: set = set()

while ((msg := input()) != ""):
    fauna_lst = msg.split()

    total_animal = len(fauna_lst)

    if total_animal == 1:
        continue

    for i in range(total_animal):
        if fauna_lst[i] == "зайка":
            if i == 0:
                near_bunny.add(fauna_lst[1])
            elif (i + 1) == total_animal:
                near_bunny.add(fauna_lst[i - 1])
            else:
                near_bunny.add(fauna_lst[i - 1])
                near_bunny.add(fauna_lst[i + 1])

for item in near_bunny:
    print(f"{item}")
            