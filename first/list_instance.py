class ListInstance:
    def __init__(self):
        self._val = '0'
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += f"\t{attr} = {self.__dict__[attr]}\n"
        return result

    def __str__(self):
        return f"\tInstance of {self.__class__.__name__}, adress {id(self)}:\n{self.__attrnames()}"


if __name__ == '__main__':
    x = ListInstance()
    print(x)
