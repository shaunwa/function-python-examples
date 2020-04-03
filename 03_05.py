numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

doubled = [x * 2 for x in numbers_list]
print(doubled)

evens = [x for x in numbers_list if x % 2 == 0]
print(evens)