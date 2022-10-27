from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass


class Triangle(Polygon):
    def sides(self):
        print("3 sides")


class Pentagon(Polygon):
    def sides(self):
        print("5 sides")


class Hexagon(Polygon):
    def sides(self):
        print("6 sides")


if __name__ == '__main__':
    R = Triangle()
    R.sides()

    R = Pentagon()
    R.sides()

    K = Hexagon()
    K.sides()
