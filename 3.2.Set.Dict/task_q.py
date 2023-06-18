friends = dict()

while ((names := input()) != ""):
    n1, n2 = names.split()

    if friends.get(n1) is None:
        friends[n1] = [n2]
    else:
        friends[n1] += [n2]

    if friends.get(n2) is None:
        friends[n2] = [n1]
    else:
        friends[n2] += [n1]

friends2level = dict()
for key, values in friends.items():
    
    friends2level[key] = list()

    for item in values:

        sub_frnd_lst: list = friends[item]

        for item2 in sub_frnd_lst:
            if item2 == key:
                continue
            friends2level[key] += [item2]

for i in sorted(friends2level):
    print(f"{i}: ", end="")
    print(f"{', '.join(sorted(set(friends2level[i])))}")

    