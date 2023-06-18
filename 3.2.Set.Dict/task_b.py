a: str = input()
b: str = input()

print((", ".join(set(a) & set(b))).replace(", ", ""))