
class Wrapped:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, item):
        print('getattr: ' + item)
        return getattr(self.wrapped, item)

