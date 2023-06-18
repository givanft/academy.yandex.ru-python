n: int = int(input())

products = set()
while (n > 0):    
    products.add(input())
    n -= 1

m: int = int(input())

recipe_lst: list = []

while (m > 0):
    recipe = input()
    n_recipe = int(input())

    tmp: int = n_recipe
    ingred = set()
    while (tmp > 0):
        ingred.add(input())
        tmp -= 1

    if len(products & ingred) == n_recipe:
        recipe_lst.append(recipe)

    m -= 1

if len(recipe_lst) == 0:
    print("Готовить нечего")
else:
    for item in sorted(recipe_lst):
        print(f"{item}")