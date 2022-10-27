class Cat():
    def __init__(self, cat):
        print(cat, 'walks')


class Dog(Cat):
    def __init__(self, dog):
        print(dog, 'runs')
        super().__init__(dog)


if __name__ == '__main__':
    d1 = Dog('Dog')
