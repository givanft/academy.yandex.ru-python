alphabet: dict = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
                  'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
                  'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
                  'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
                  'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA'}

msg: str = input()
msg_out: str = ""

for ch in msg:

    if ch.upper() == 'Ъ' or ch.upper() == 'Ь':
        continue

    if alphabet.get(ch.upper()) is None:
        msg_out += ch
        continue

    if ch.islower():
        msg_out += alphabet[ch.upper()].lower()
    else:
        msg_out += alphabet[ch].lower().capitalize()
    
print(f"{msg_out}")
