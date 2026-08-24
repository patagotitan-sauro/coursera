#!/home/rouse/Scrips/pythonDesign/.venv_coursera/bin/python
"""
The ISP advocates for designing smaller, more specific interfaces rather than broad, general-purpose ones.
This principle states that a class should not be forced to implement interfaces it does not use.
In the context of Python, this implies that a class shouldn't be forced to inherit and implement methods
that are irrelevant to its purpose.

Note: Note about interfaces. 
To understand the importance of interfaces and the techniques we use in Python to define them 
(abstract base classes, protocols, etc.), in particular,
here is the situation where protocols are the natural answer,
that is, they help define small interfaces where each interface is created for doing only one thing.
"""

from typing import Protocol
class Printer(Protocol):
    def print_document(self):
        ...
class Scanner(Protocol):
    def scan_document(self):
        ...
class Fax(Protocol):
    def fax_document(self):
        ...
class AllInOnePrinter:
    def print_document(self):
        print("Printing")
        
    def scan_document(self):
        print("Scanning")
        
    def fax_document(self):
        print("Faxing")
class SimplePrinter:
    def print_document(self):
        print("Simply Printing")
def do_the_print(printer: Printer):
    printer.print_document()
if __name__ == "__main__":
    all_in_one = AllInOnePrinter()
    all_in_one.scan_document()
    all_in_one.fax_document()
    do_the_print(all_in_one)
    
    simple = SimplePrinter()
    do_the_print(simple)
