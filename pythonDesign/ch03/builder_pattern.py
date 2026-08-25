#!/home/rouse/Scrips/coursera/pythonDesign/.venv/bin/python

"""
# The Builder Pattern

We just covered the first two creational patterns, the factory method and the abstract factory, which both offer approaches to improve the way we create objects in nontrivial cases.

## Real-world Examples

In our everyday life, the builder design pattern is used in fast-food restaurants. 
The same procedure is always used to prepare a burger and the packaging (box and paper 
bag), even if there are many kinds of burgers (classic, cheeseburger, and more) 
and different packages (small-sized box, medium-sized box, and so forth). 
The difference between a classic burger and a cheeseburger is in the representation and not in the construction procedure. In this case, the director is the cashier who gives instructions about what needs to be prepared to the crew, and the builder is the person from the crew who takes care of the specific order.

## Comparison with the Factory Pattern

At this point, the distinction between the builder pattern and the factory pattern might not be very clear. The main difference is that a factory pattern creates an object in a single step, whereas a builder pattern creates an object in multiple steps and almost always uses a director.

The pattern is also beneficial when the object's construction process is more complex than simply setting initial values. For example, if an object's full creation involves multiple steps, such as parameter validation, setting up data structures, or even making calls to external services, the builder pattern can encapsulate this complexity.
"""
import time
from enum import Enum

PizzasProgress = Enum("PizzasProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum( "PizzaTopping", "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano",)
STEP_DELAY = 3

class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []


    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f"preparing {self.dough.name} dough for {self.name} pizza...")
        time.sleep(STEP_DELAY)
        print(f"done with the {self.dough.name} dough")

class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza("magerita")
        self.progress = PizzasProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzasProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print("adding tomato sauce")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print("done with the tomato sauce")

    def add_topping(self):
        topping_desc = "double mozzarella, oregano"
        topping_items = (PizzaTopping.double_mozzarella, PizzaTopping.oregano)
        print(f"adding the topping ({topping_desc}) to the margarita pizza")
        self.pizza.topping.extend(topping_items)
        time.sleep(STEP_DELAY)
        print(f"done with the topping ({topping_desc})")

    def bake(self):
        self.progress = PizzasProgress.baking
        print(f"baking the {self.pizza} pizza for {self.baking_time} seconds")
        time.sleep(self.baking_time)
        self.progress = PizzasProgress.ready
        print(f"the {self.pizza} pizza is ready")



class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza("creamy bacon")
        self.progress = PizzasProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzasProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

class Waiter:
    def __init__(self):
        self.builder = None


    def construct_pizza(self, builder):
        self.builder = builder
        steps = (
            builder.prepare_dough,
            builder.add_sauce,
            builder.add_topping,
            builder.bake,
            )

        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza

def validate_style(builders):
    try:
        input_msg = "What pizza would you like? [m]argeritha or [c]reamy bacon?"
        pizza_style = input(input_msg)
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError:
        error_msg = "Sorry, only margarita (key m) and creamy bacon (key c) are available"
        print(error_msg)
        return (False, None)
    return (True, builder)

def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
        print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f"Enjoy your {pizza}!")

if __name__ == "__main__":
    main()
"""
Here is a summary of the implementation:

    We start with a couple of imports we need, for the standard Enum class and time module.

    We declare variables for a few constants: PizzaProgress, PizzaDough, PizzaSauce, PizzaTopping, and STEP_DELAY.

    We define our Pizza class.

    We define classes for two builders, MargaritaBuilder and CreamyBaconBuilder.

    We define our Waiter class.

    We add a validate_style() function to improve things regarding exception handling.

    Finally, we have the main() function, followed by a snippet for calling it when the program is run. In the main() function, the following happens:

        We make it possible to choose the pizza builder based on the user's input, after validation via the validate_style() function.

        The pizza builder is used by the waiter for preparing the pizza.

        The created pizza is then delivered.
"""



