import sys
sys.setrecursionlimit(1000)

class Object:
    def __init__(self, a, b, c):
        self.a = a  # Public
        self._b = b  # Protected
        self.__c = c  # Private

    # Getter для protected
    @property
    def b(self):
        return self._b

    # Getter для private - ничем не отличается
    @property
    def c(self):
        return self.__c


obj = Object(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
