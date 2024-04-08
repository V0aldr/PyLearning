def square(arg):
    return arg ** 2


class Sum:

    def __init__(self, val):
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Project:
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


sobj = Sum(2)
pobj = Project(3)
args = (square, sobj, pobj.method)

for arg in args:
    print(arg(5))
