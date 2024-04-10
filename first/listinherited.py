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

    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr.startswith('__') and attr.endswith('__'):
                result += f'\t{attr}\n'
            else:
                result += f"\t{attr} = {getattr(self, attr)}\n"
        return result

    def __str__(self):
        return (f"<Instance of {self.__class__.__name__}, adress: {id(self)}>\n"
                f"{self.__attrnames()}")

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)

