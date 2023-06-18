empty_set: set = set()
vowels: set = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}

for i in vowels:
    print(f"{i}", end=" ")

print("\n-------------------")

word = "коллекция"
print(f"{set(word)}", end="")

print("\n -------------------")

s1: set = {1, 2, 3}
s2: set = {3, 4, 5}
print(f"{s1 | s2}") # union
print(f"{s1 & s2}") # intersection
print(f"{s1 - s2}") # difference
print(f"{s1 ^ s2}") # symmetric_difference

print("\n -------------------")

s1: set = {1, 2, 3}
s2: set = {3, 1, 2}
print(f"{s1 == s2}")

s1: set = {1, 2, 3}
s2: set = {1, 2, 3, 4}
print(f"{s1 <= s2}")
print(f"{s2 >= s1}")

print("\n -------------------")

s = set()
s.add(1)
s.remove(1) # KeyError otherways
s.discard(2) # remove if exists
x = s.pop() # get and remove random element
set.clear()