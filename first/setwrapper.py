class Set:
    """
    Класс имуитирует поведение типа set()
    """

    def __init__(self, value: list = []):
        self.data = []
        self.concat(value)

    def intersect(self, other: list):
        res = [x for x in self.data if x in other]
        return Set(res)

    def union(self, other):
        res = self.data[:]
        res = [x for x in other if x not in res]
        return Set(res)

    def concat(self, other):
        self.data += [x for x in other if x not in self.data]

    def __len__(self): return len(self.data)

    def __getitem__(self, key): return self.data[key]

    def __and__(self, other): return self.intersect(other)  # self & other

    def __or__(self, other): return self.union(other)

    def __repr__(self): return 'Set:' + repr(self.data)

    def __iter__(self): return iter(self.data)
