"""
Модуль содержит подкласс Множества
"""


class Set(list):

    def __init__(self, value=[]):
        list.__init__(self)
        self.concat(value)

    def intersect(self, other: list):
        res = [x for x in self if x in other]
        return Set(res)

    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res

    def concat(self, other):
        for x in other:
            if x not in self:
                self.append(x)

    def __and__(self, other): return self.intersect(other)

    def __or__(self, other): return self.union(other)

    def __repr__(self): return 'Set:' + list.__repr__(self)


if __name__ == '__main__':
    x = Set([1, 3, 5, 7])
    y = Set([2, 1, 4, 5, 6])
    print(x, y, f"{len(x) = }", sep='\n')
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse(); print(x)


