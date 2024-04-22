def tracer(func, calls=0):
    def oncall(*args):
        nonlocal calls
        calls += 1
        print(f"call {calls} to {func.__name__}")
        return func(*args)
    return oncall


class C:

    @tracer
    def spam(self, a, b, c): return a + b + c


x = C()
print(x.spam(1, 2, 3))
print(x.spam('a', 'b', 'c'))
