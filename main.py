from function import get_formatted_name

first = input("Введите имя: ")

last = input("Теперь фамилию: ")

formatted_name = get_formatted_name(first, last)
print("Вас зовут: " + formatted_name + '.')
