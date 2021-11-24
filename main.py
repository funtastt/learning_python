# Распаковка последовательности

massive = [1, 2, 3, 4, 5]

a, b, *c = massive
d, *e, f = massive
*g, h, i = massive
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5]
print(d)  # 1
print(e)  # [2, 3, 4]
print(f)  # 5
print(g)  # [1, 2, 3]
print(h)  # 4
print(i)  # 5

