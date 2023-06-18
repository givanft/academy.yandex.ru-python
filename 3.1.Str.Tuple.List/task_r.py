msg: str = input()

char: str = msg[0]
char_total: int = 1
rng: int = len(msg)

for item in range(1, rng):
    if char == msg[item]:
        char_total += 1
    else:
        print(f"{char} {char_total}")
        char = msg[item]
        char_total = 1

print(f"{char} {char_total}")
