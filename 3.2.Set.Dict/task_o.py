nums: list = input().split()

mega_lst: list = []
for num in nums:
    binary = bin(int(num))[2:]

    dnum: dict = {}

    dnum["digits"] = len(binary)
    dnum["units"] = binary.count('1')
    dnum["zeros"] = binary.count('0')

    mega_lst.append(dnum)

print(f"{mega_lst}")