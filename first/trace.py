
class Wrapped:
    NAME = 'qwerty'
    def __init__(self, object):
        self.wrapped = object
        self.__enigma = 0
        self._alarm = '_'

    def __getattr__(self, item):
        print('getattr: ' + item)
        return getattr(self.wrapped, item)



x = Wrapped('spam')

print(x.__dict__.items())
x._Wrapped__enigma = 10
print(x.__dict__.items())