class A: pass
class B(A): pass
class C1(A): pass
class C2: pass
class D1(B, C1): pass
class D2(B, C2): pass

X = list(D1.__mro__)
Y = list(D2.__mro__)
print(X[3] is Y[2])
