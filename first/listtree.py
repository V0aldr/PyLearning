class ListTree:
    """
    Подмешиваемый класс, который возвращает в __ str__ результат обхода целого
    дерева классов и атрибуты всех его объектов, начиная с self и выше;
    запускается print () и str() и возвращает сформированную строку;
    использует схему именования атрибутов _ X, чтобы избежать конфликтов
    имен в клиентах; явно рекурсивно обращается к суперклассам,
    для ясности применяет str.format().
    """

    def __attrname(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__visited):
            if attr.startswith('__') and attr.endswith('__'):
                result += f"{spaces}{attr}\n"
            else:
                result += f"{spaces} {attr} = {getattr(obj, attr)}"
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return f"\n{dots} < Class: {aClass.__name__}, adress: {id(aClass)} (see above)>\n"
        else:
            self.__visited[aClass] = True
            here = self.__attrname(aClass, indent)
            above = ''
            for super in aClass.__bases__:
                above += self.__listclass(aClass, indent + 4)
            return f"\n{dots} <Class: {aClass.__name__}, address {id(aClass)}:\n{here}{above}{dots}>\n"

    def __str__(self):
        self.__visited = {}
        here = self.__attrname(self, 0)
        above = self.__listclass(self.__class__, 4)
        return f'<Instance of {self.__class__.__name__}, address {id(self)}:\n{here}{above}>'

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListTree)






