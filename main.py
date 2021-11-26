class A:
    def __init__(self, value):
        self.value = value

    # Throws exception if class doesn't have required key
    def __setattr__(self, key, value):
        if key == "value":
            self.__dict__[key] = value
        else:
            raise AttributeError


a = A(1)
a.value = 23
a.value2 = 24
