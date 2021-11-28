# Function decorator
def track_exceptions_decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello from wrapper!")
        return func(*args)

    return wrapper


# Class decorator
def track_exception(cls):
    callable_attributes = {k: v for k, v in cls.__dict__.items()
                           if callable(v)}
    for name, func in callable_attributes.items():
        decorated = track_exceptions_decorator(func)
        setattr(cls, name, decorated)
    return cls


@track_exception
class A:
    def f1(self):
        print('1')

    def f2(self):
        print('2')


a = A()
a.f1()
a.f2()
