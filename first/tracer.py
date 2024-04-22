class tracer:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"call {self.calls} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@tracer
def spam(a, b, c):
    return a + b + c

@tracer
def say_hello(message):
    return f"Say {message}!"


print(spam('a', 'b', 'c'))
print(spam(1, 2, 3))
print(say_hello('Ky, optom'))
