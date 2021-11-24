class Object:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return str(self.name) + ": " + str(self.value)


# Список - массив ссылок на объекты
test_list = [Object("Name", 32), 3405, "hello"]
print(test_list)  # Выводит - [<__main__.Object object at 0x00000139E226FFD0>, 3405, 'hello']
test_list = list(map(str, test_list))
print(test_list) # Выводит - ['Name: 32', '3405', 'hello']