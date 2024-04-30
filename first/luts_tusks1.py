class Adder:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        if isinstance(self.data, list):
            if isinstance(other, list):
                return self.data.extend(other)
            else:
                return self.data.append(other)
        if isinstance(self.data, dict):
            if isinstance(other, dict):
                self.data = self.data | other
                return self.data
            else:
                # self.data['other'] = other
                # self.data.setdefault(str(other), other)
                return self.data.update({f"{other}": other})


class ListAdder(Adder): pass


class DictAdder(Adder): pass


x = ListAdder([1])
x + 1
print(x.data)
x + [1]
print(x.data)

y = DictAdder({'y': 'y'})
print(y.data)
y + {'x': 'x'}
print(y.data)
y + 1
print(y.data)
y + [1]
print(y.data)



print('Ok')
