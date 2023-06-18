msg: str = "10 15 - 7 *"

lst: list = msg.split()

i: int = -1

while len(lst) > 1:
    i += 1
      
    if i < 2:
        continue

    pos: int = i - 2    
    a: int = lst[pos]
    b: int = lst[pos + 1]
    c: int = 0
    
    match lst[i]:
        case '*':
            c = int(a) * int(b)
        case '+':
            c = int(a) + int(b)
        case '-':
            c = int(a) - int(b)
        case _:    
            continue

    del lst[pos:pos + 3]
    lst.insert(pos, c)
    i = -1

print(f"{lst[0]}")
