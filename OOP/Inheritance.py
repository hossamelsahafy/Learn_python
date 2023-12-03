#!/usr/bin/python3
class food:
    def __init__(self, name, price, amount):
        self.name = name

        self.price = price

        self.amount = amount
        print(f"{self.name} was created from base class")

    def eat(self):
        print("Eat Method From Base Class")


class Apple(food):
    def __init__(self, name, price, amount):
        # food.__init__(self, name)

        super().__init__(name, price, amount)
        print(
            f"{self.name} was created from base Derived class and price is {self.price} and amount is {self.amount}"
        )

    def get_from_tree(self):
        print("Get From Tree from derived class")


# food_two = Apple()
food_two = Apple("pizza", 150, 233)
food_two.eat()
food_two.get_from_tree()
