countries_and_capitals: dict = {"Россия": "Москва", "США": "Вашингтон", "Франция": "Париж"}

if "Сербия" in countries_and_capitals:
    print(countries_and_capitals["Сербия"])
else:
    print("Страна пока не добавлена в словарь", end="")

print("\n -------------------")

countries_and_capitals["Сербия"] = "Белград"
print(countries_and_capitals, end="")

print("\n -------------------")

for country in countries_and_capitals:
    print(f"У страны {country} столица — {countries_and_capitals[country]}.", end="")

print("\n -------------------")

d: dict = {"a": 1, "b": 2, "c": 3}
len(d)      # => 3
d.get("e", "Ключа нет в словаре") # get default if 'e' is ebsent ||| 
# countries[country] = countries.get(country, []) + [str_number] 
# => Если страна country есть среди ключей, то get() возвращает список, хранящийся по этому ключу, иначе get() возвращает пустой список. 
# Добавляем в список значение str_number.

for key, value in d.items():
    print(key, value) # => a 1 b 2 c 3

for key in d.keys():
    print(key) # => a b c

for value in d.values():
    print(value) # => 1 2 3

x = d.pop("a") # get value and remove 'a'
del d["b"]  # remove d, KeyError otherways
d.clear()

# Add LIST to dict:
sad = {}
sad["Горшенин"] = ["Иван"]
sad["Горшенин"] += ["Сергей"] # => {'Горшенин': ['Иван', 'Сергей']}

# sorted(key_value) returns an iterator over the
# # Dictionary’s value sorted in keys.
key_value = {}
key_value[2] = 56
key_value[1] = 2
for i in sorted(key_value):
    print((i, key_value[i]), end=" ")
