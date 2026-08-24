#!//home/rouse/Scrips/pythonDesign/.venv_coursera/bin/python
"""
The OCP is another fundamental principle in software design. 
It emphasizes that software entities, such as classes and modules, should be open for extension but closed for modification. 
What does that mean? It means that once a software entity is defined and implemented, 
it should not be changed to add new functionality. 
Instead, the entity should be extended through inheritance or interfaces to accommodate new requirements and behaviors.

Things work fine! 
The main win is that we were able to define a new shape without modifying the calculate_area function. 
The new design is elegant and allows ease of maintenance thanks to following the OCP.
"""

import math
from typing import Protocol


class Shape(Protocol):
    def area(self) -> float:
        ...
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height
    def area(self) -> float:
        return self.width * self.height
class Circle:
    def __init__(self, radius: float):
        self.radius: float = radius
    def area(self) -> float:
        return math.pi * (self.radius**2)
def calculate_area(shape: Shape) -> float:
    return shape.area()
if __name__ == "__main__":
    rect = Rectangle(12, 8)
    rect_area = calculate_area(rect)
    print(f"Rectangle area: {rect_area}")
    circ = Circle(6.5)
    circ_area = calculate_area(circ)
    print(f"Circle area: {circ_area:.2f}")
