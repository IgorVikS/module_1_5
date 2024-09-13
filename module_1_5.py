immutable_var = 1, 2, 3, 'a', 'b', 'c'
print(immutable_var)

# immutable_var = 1, 2, 3, 'a', 'b', 'c'
# immutable_var[0] = 5   кортеж не поддерживает обращение по элементам
# print(immutable_var)  TypeError: 'tuple' object does not support item assignment

mutable_list = [1, 2, 3, 'a', 'b', 'c', 'Modifieds']
print(mutable_list)

mutable_list = [1, 2, 3, 'a', 'b', 'c'], (0)
mutable_list[0][4] = 7
print(mutable_list)
