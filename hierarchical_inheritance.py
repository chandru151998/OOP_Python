class Mammal():
    def __init__(self, mammal):
        print(mammal, 'is a warm-blooded animal.')


class NonWingedMammal(Mammal):
    def __init__(self, non_winged):
        print(non_winged, "can't fly.")
        super().__init__(non_winged)


class NonMarineMammal(Mammal):
    def __init__(self, non_marine):
        print(non_marine, "can't swim.")
        super().__init__(non_marine)


class Dog(Mammal):
    def __init__(self, dog):
        print(dog, "has 4 legs")
        super().__init__(dog)


if __name__ == '__main__':
    d = Dog('Dog')
    bat = NonMarineMammal('Bat')
