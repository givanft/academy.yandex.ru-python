while (name := input("Введите имя: ")) != "СТОП":
    print(f"Привет, {name}!")
print("Программа завершена.")

### range(n)        # return [0..n-1] => range(4): 0, 1, 2, 3;
### range(k, n)     # return [k..n-1] => range(1, 5): 1, 2, 3, 4;
### range(k, n, s)  # return [k..n-1] with step s => (1, 10, 2): 1, 3, 5, 7, 9.
### range(5, -1, -1)# return revers: 5 4 3 2 1 0


