"""
Обобщенный инструмент тестирования подмешиваемых классов вывода списков:
он похож на средство транзитивной перезагрузки модулей из главы 25 первого
тома, но ему передается объект класса (не функции), а в testByNames
добавлена загрузка модуля и класса по строковым именам в соответствии с
паттерном проектирования 'Фабрика’.
"""

import importlib


def tester(listerclass, sept=False):
    class Super:                    # Метод__ init__ суперкласса
        def __init__(self):         # Создать атрибуты экземпляра
            self.data1 = 'spam'

        def ham(self): pass

    class Sub(Super, listerclass):  # Подмешивание ham и__ str__

        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self): pass

    instance = Sub()
    print(instance)
    if sept: print('-'*80)

def test_by_name(modname, classname, sept=False):
    modobject = importlib.import_module(modname)
    print(modobject)
    listerclass = getattr(modobject, classname)
    tester(listerclass, sept)

if __name__ == '__main__':
    test_by_name('list_instance', 'ListInstance', True)
    test_by_name('listinherited', 'ListInherited', True)
    # test_by_name('listtree', 'ListTree', False)
