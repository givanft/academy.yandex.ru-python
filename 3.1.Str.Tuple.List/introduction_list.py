print("\n -------------------")

numbers = [10, 20, 30, 40, 50]
print(numbers[0])       # 10
print(numbers[-1])      # 50
print(numbers[1:3])     # [20, 30]
print(numbers[::-1])    # [50, 40, 30, 20, 10]

print("\n -------------------")

countries_and_capitals: list = [("Россия", "Москва"), ("США", "Вашингтон"), ("Франция", "Париж")]
type(countries_and_capitals)
print(f"{countries_and_capitals}", end="")

print("\n -------------------")

for country in countries_and_capitals:
    if country[0] == "Франция":
        print(country[1], end="")
        break

print("\n -------------------")

# [1, 2] + [3, 4, 5]        => [1, 2, 3, 4, 5]
# [1, 2, 3] * 3             => [1, 2, 3, 1, 2, 3, 1, 2, 3]
# len([1, 2, 3])            => 3
# [1, 2].append(3)          => [1, 2, 3]
# [1, 2, 3].clear()         => []
# [1, 2, 3].extend([4, 5])  => [1, 2, 3, 4, 5]
# [1, 3, 4].insert(1, 2)    => [1, 2, 3, 4]
# x = [1, 2, 3].pop()       => 3    [1, 2]
# [1, 2, 3].reverse()       => [3, 2, 1]
# [2, 3, 1].sort()          => [1, 2, 3]
# [1, 1, 1, 2, 3, 1].count(1)   => 4
# [1, 2, 3, 2, 1].remove(2)     => [1, 3, 2, 1]
# del a[0]  => remove first item

