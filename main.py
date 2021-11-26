from functools import reduce

# functools.reduce() - обрабатывает массив и приводит его к одному значению-результату (сумме, строке или др.)
# lambda - ничего особенного, так же как в Java


def avg(massive):
    return reduce(lambda a, b: a + b, massive) / len(massive)


mass = [i ** 2 for i in range(0, 5)]

print(mass)
print(avg(mass))
