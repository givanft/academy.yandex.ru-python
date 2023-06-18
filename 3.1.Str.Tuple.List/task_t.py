msg: str = "7 3 + ~"

lst: list = msg.split()

i: int = -1

while len(lst) > 2:
    i += 1
      
    if i < 2 and str(lst[1]).isdigit():
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
        case '/':
            c = int(a) // int(b)
        case '~':
            c = int(b) * (-1)
            lst[pos + 1] *= -1
        case '!':
            c = int(b)
            k: int = 1
            for j in range(1, c):
                k *= j
            del lst[i]
            del lst[i - 1]
            lst.insert(i - 1, k)
            i = -1
            continue
        case '#':
            del lst[i]
            lst.insert(i, b)
            i = -1
            continue
        case '@':  
            c = lst[pos - 1]
            del lst[pos - 1:pos + 3]
            lst.insert(pos - 1, a)
            lst.insert(pos, b)
            lst.insert(pos + 1, c) 
            i = -1
            continue 
        case _:    
            continue

    del lst[pos:pos + 3]
    lst.insert(pos, c)
    i = -1

if len(lst) > 1:
    if lst[1] == '~':
        lst[0] = int(lst[0]) * -1
    elif lst[1] == "!":
        k: int = 1
        for i in range(1, int(lst[0])):
            k *= i
        lst[0] = k

print(f"{lst[0]}")
