class Property:
    def get_age(self):
        return 40
    def set_age(self, value):
        print(f"setage: {value}")
        self._age = value

    age = property(get_age, set_age)

p = Property()
print(f"{p.age = }")    # Запускается getage
                        # bound method called age.property
p.age = 50              # Запускается setage
print(f"{p.age = }")
print(f"{p._age = }")


p.job = 'trainer'       # Нормальное присваивание: setage не вызывается
print(f"{p.job = }")            # Нормальное извлечение: getage не вызывается