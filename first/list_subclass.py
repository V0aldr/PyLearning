class MyList(list):
    def __getitem__(self, item):
        print(f"indexig {self} at {item}")
        return list.__getitem__(self, item - 1)

if __name__ == '__main__':
    print(f"{list('abc') = }")
    x = MyList('abc')                 # Метод init  унаследованный от списка
    print(f"x.__repr__  => {x}")      # Метод repr , унаследованный от списка
    print(f"{'EXPL':-^50}")
    print(x[1])
    print(x[3])
    x[5] = 1
    print(x)
    print(f"{'EXPL':-^50}")
    x.append('spam')
    print(x)
    print(f"{'EXPL':-^50}")
    x.reverse()
    print(x)
