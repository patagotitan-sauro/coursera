#!/home/rouse/Scrips/pythonDesign/.venv_coursera/bin/python

from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def do_something(self, param:str):
        pass

class MyClass(MyInterface):
    def do_something(self, param: str):
        print(f"Do something whith: '{param}'")


if __name__ == "__main__":
    MyClass().do_something("some param")

