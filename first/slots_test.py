""" Проверка работоспособости __slots__"""

import timeit


base = """
Is = []
for x in range(1000):
    x = C()
    x.a, x.b, x.c, x.d = 1, 2, 3, 4
    t = x.a + x.b + x.c + x.d
    Is.append(t)
"""

stmt = """
class C:
    __slots__ = ['a', 'b', 'c', 'd']
""" + base

print("Slots: ", end=' ')   # Co слотами
print(min(timeit.repeat(stmt, number=1000, repeat=3)))

stmt = """
class C: pass
""" + base

print("NonSlots: ", end=' ')    # Без слотов
print(min(timeit.repeat(stmt, number=1000, repeat=3)))
