# Короче, это как Map в Java
# Ключ - какая-то строка String
# Значение - что угодно (строка, число, объект, еще один словарь, список паролей Google...)
dictionary = {
    'name': "dict",
    'value': 23324
}
dictionary2 = {
    'name': "dict2",
    'value': 5,
    'refer': dictionary
}
print(dictionary2)
