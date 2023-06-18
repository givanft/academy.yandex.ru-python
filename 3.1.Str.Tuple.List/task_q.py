msg: str = input().lower().replace(" ", "")
answ: str = "YES"

for i in range(len(msg) // 2):
    if msg[i] != msg[-(i + 1)]:
        answ = "NO"
        break
    
print(answ)