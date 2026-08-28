#!/home/rouse/Scrips/coursera/pythonDesign/.venv/bin/python
"""
The Object Pool Pattern

The object pool pattern is a creational design pattern that allows you to reuse existing objects instead of creating 
new ones when they are needed. This pattern is particularly useful when the cost, in terms of system resources, 
time, and so on of initializing a new object is high.

Real-world Examples

Consider a car rental service. When a customer rents a car, the service doesn't manufacture a new car for them. 
Instead, it provides one from a pool of available cars. Once the customer returns the car, it goes back into the pool, 
ready to be used by the next customer. 
Another example would be a public swimming pool. Rather than filling the pool with water every time someone wants to swim, 
the water is treated and reused for multiple swimmers. This saves both time and resources.


"""

class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.in_use = False


class CarPool:
    def __init__(self):
        self._available = []
        self._in_use = []

    def acquire_car(self) -> Car:
        if len(self._available) == 0:
            new_car = Car("BMW", "M3")
            self._available.append(new_car)
        car = self._available.pop()
        self._in_use.append(car)
        car.in_use = True
        return car

    # We then add a method that handles things when a client releases a car, as follows:
    def release_car(self, car: Car) -> None:
        car.in_use = False
        self._in_use.remove(car)
        self._available.append(car)

if __name__ == "__main__":
    pool = CarPool()
    car_name = "Car 1"
    print(f"Acquire {car_name}")
    car1 = pool.acquire_car()
    print(f"{car_name} in use: {car1.in_use}")
    print(f"Now release {car_name}")
    pool.release_car(car1)
    print(f"{car_name} in use: {car1.in_use}")