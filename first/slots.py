class D:
    __slots__ = ['a', 'b', '__dict__']  # Указание__ diet__ для его включения
    c = 3                               # Атрибуты класса работают нормально

    def __init__(self):
        self.d = 4                      # d хранится в __dict__ , а является слотом


d = D()
print(f"{d.d = }")
print(f"{d.c = }")
# print(f"{d.a = }")                            # AttributeError: 'D' object has no attribute 'a'
d.a = 1                                         # из-за присутствия __dict__ в __slots__ динамически доб-ся "a" & "b"
d.b = 5
print(f"{d.a = }")
print(f"{d.b = }")
print('-' * 20)
print(f"{d.__dict__ = }")
print(f"{d.__slots__ = }")
print(f"{'getattr: ':-^40}")
print(getattr(d, 'a'), getattr(d, 'c'), getattr(d, 'd'), sep='\n')
