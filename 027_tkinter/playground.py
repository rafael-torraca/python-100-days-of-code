def add(*args):
    total = 0
    for n in args:
        total += n
    return total


law = add(10, 10, 10)

print(law)


def calculate(**kwargs):
    # for key, value in kwargs.items():
    #     print(key, value)
    n = 2
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(add=3, multiply=2))

class Car:

    def __init__(self, **kw):
        """make and model"""
        self.make = kw["make"] # not recomended! error
        self.model = kw.get("model") #better way return none if not informed


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
