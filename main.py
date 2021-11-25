import test
import importlib

test.first = 43534534
test.second = 123
test.third = "Hello"

print(test.first)
print(test.second)
print(test.third)

importlib.reload(test)  # Заново импортирует библиотеку, модуль

print(test.first)
print(test.second)
print(test.third)
