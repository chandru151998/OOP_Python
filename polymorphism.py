#Method overloading
# class Multiply():
#     def product(self, a, b):
#         p = a * b
#         print(p)
#
#     def product(self, a, b, c):
#         p = a * b * c
#         print(p)
#
#
# if __name__ == '__main__':
#     m = Multiply()
#     m.product(4, 5, 5)


# Method overriding
class Parent1():
    def show(self):
        print("Parent1")


class Parent2():
    def display(self):
        print("Parent2")


class Child(Parent1, Parent2):
    def show(self):
        print("Child")


if __name__ == '__main__':
    obj = Child()

    obj.show()
    obj.display()
