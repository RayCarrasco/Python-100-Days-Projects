def add(*args):
    print(type(args))
    print(f"Total: {sum(args)}")


add(1, 2, 3, 4, 5, 6, 7, 8, 9)


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

operations = {"add": add}


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.models = kw.get("model")


my_carr = Car(make="Nissan")
print(my_carr.make, my_carr.models)

print("***")
operations["add"](1, 2, 3)
