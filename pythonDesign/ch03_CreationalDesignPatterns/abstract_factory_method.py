#!/home/rouse/Scrips/pythonDesign/.venv_coursera/bin/python
"""
# The Abstract Factory Pattern

The abstract factory pattern is a generalization of the factory method idea. 
Basically, an abstract factory is a (logical) group of factory methods, where each 
factory method is responsible for generating a different kind of object.

# Real-world Examples

The abstract factory is used in car manufacturing. The same machinery is used for stamping the parts (doors, panels, hoods, fenders, and mirrors) of different car models. The model that is assembled by the machinery is configurable and easy to change at any time.

# Use Cases for the Abstract Factory Pattern
Since the abstract factory pattern is a generalization of the factory method pattern, it offers the same benefits: it makes tracking an object creation easier, it decouples object creation from object usage, and it gives us the potential to improve the memory usage and performance of our application.
"""
class Frog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}!"
        print(msg)

class Bug:
    def __str__(self):
        return "a bug"
    def action(self):
        return "eats it"

class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return "\t------ Frog World -------"
    def make_character(self):
        return Frog(self.player_name)
    def make_obstacle(self):
        return Bug()

##
##

class Wizard:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Wizard battles against {obstacle} and {act}!"
        print(msg)

class Ork:
    def __str__(self):
        return "an evil ork"
    def action(self):
        return "kills it"

class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return "\t------ Wizard World -------"

    def make_character(self):
        return Wizard(self.player_name)
    def make_obstacle(self):
        return Ork()

##########

class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name):
    age = None
    try:
        age_input = input(f"Welcome {name}. How old are you? ")
        age = int(age_input)
    except ValueError:
        print(f"Age {age} is invalid, please try again...")
        return False, age
    return True, age

def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()

if __name__ == "__main__":
    main()
