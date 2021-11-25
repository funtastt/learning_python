def parent(parent_value):
    parent = parent_value
    def child(child_value):
        nonlocal parent
        parent += 1
        child = child_value
        return str(parent) + " - " + str(child)

    return child


for i in range(0, 10):
    F = parent(i)
    for j in range(0, 10):
        print(F(j))
