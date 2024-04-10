class ListInherited:
    """
    Применяет dir() для сбора атрибутов экземпляра и имен, унаследованных
    из его классов;
    в Python З.Х отображается больше имен, чем в Python 2.Х из-за наличия
    подразумеваемого суперкласса object в модели классов нового стиля;
    getattr() извлекает унаследованные имена не в self.__dict__ ;
    используйте __str__ , а не __rерr__ , иначе произойдет зацикливание при
    вызове связанных методов!
    """

    def __attrnames(self, indent=' '*4):
        unders = []
        # result = f"Unders{'-'*77}\n{indent}{', '.join(unders)}\nOthers{'-'*77}\n"
        result = 'Unders%s\n%s%%s\nOthers%s\n' % ('-'*77, indent, '-'*77)
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:82 - (len(indent) - len(attr))]
                result += f"{indent}{attr} = {display}\n"
        return result % ', '.join(unders)

    def __str__(self):
        return (f"<Instance of {self.__class__.__name__}, adress: {id(self)}>\n"
                f"{self.__attrnames()}")


if __name__ == '__main__':
    import testmixin

    testmixin.tester(ListInherited)
    print()
