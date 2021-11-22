# Статическая типизация - в Java, C++, C#  т.д.
# Динамическая типизация - в JS, Python и т.д. - то, что нам нужно.
def get_sum(a, b):
    return a + b


print(get_sum(23, 34))
print(get_sum("23", "34"))
print(get_sum([12, 23], [34, 54]))
print(get_sum("23", 2)) # TypeError: can only concatenate str (not "int") to str

