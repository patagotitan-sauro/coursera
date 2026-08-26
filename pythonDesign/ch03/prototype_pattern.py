#!/home/rouse/Scrips/coursera/pythonDesign/.venv/bin/python
"""
The Prototype Pattern:
The prototype pattern allows you to create new objects by copying existing ones, 
rather than creating them from scratch. This pattern is particularly useful when 
the cost of initializing an object is more expensive or complex than copying an 
existing one. In essence, the prototype pattern enables you to create a new instance 
of a class by duplicating an existing instance,thereby avoiding the overhead of 
initializing a new object.

"""

import copy

class Website:
    def __init__(self,
                 name: str,
                 domain: str,
                 description: str,
                 **kwargs):
        self.name = name
        self.domain = domain
        self.description = description
        # There is a Python idiom that helps to set an arbitrary attribute named `attr` with a `val` value on an `obj` object,
        # using the setattr() built-in function: setattr(obj, attr, val).
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        summary = [ f"-{self.name} (ID: {id(self)})",]

        #NOTE: The vars() function in Python returns the dict attribute of an object. The dict attribute is a dictionary containing the
        #object's attributes (both data attributes and methods). This function is useful for debugging, as it allows you to inspect
        #the attributes and methods of an object or the local variables within a function. But note that not all objects have a dict attribute.
        #For example, built-in types such as lists and dictionaries do not have this attribute.
        infos = vars(self).items()
        ordered_infos = sorted(infos)
        for attr, val in ordered_infos:
            if attr == "name":
                continue
            summary.append(f"\t{attr}: {val}")
        return "\n".join(summary)
    
# Next, we add a Prototype class that implements the prototype design pattern. At the heart of this class, we have the clone() method,
# which is in charge of cloning the object using the copy.deepcopy() function.
#NOTE: When we clone an object using copy.deepcopy(), the memory address of the clone must be different from the memory address of the original object.
# Since cloning means that we allow setting values for optional attributes, notice how we use the setattr technique here with the attrs dictionary.
#Also, for more convenience, the Prototype class contains the register() and unregister() methods, which can be used to keep track of the cloned objects
#in a registry (a dictionary). The code of that class is as follows:

class Prototype:
    def __init__(self,):
        self.registry = {}
    def register(self, identifier: int, obj: object):
        self.registry[identifier] = obj
    def unregister(self, identifier: int):
        del self.registry[identifier]
    def clone(self, identifier: int, **attrs) -> object:
        found = self.registry.get(identifier)
        if not found:
            raise ValueError(
                f"Incorrect object identifier: {identifier}"
            )
        obj = copy.deepcopy(found)
        for key in attrs:
            setattr(obj, key, attrs[key])
        return obj

#In the main() function, which we define next, we complete the program: we clone a first Website instance, site1, to get a second object site2.
#Basically, we instantiate the Prototype class and we use its .clone() method. Then, we display the result. The code for that function is as follows:

def main():
    keywords = (
        "python",
        "programming",
        "scripting",
        "data",
        "automation",
    )
    site1 = Website(
        "Python",
        domain="python.org",
        description="Programming language and ecosystem",
        category="Open Source Software",
        keywords=keywords,
    )
    proto = Prototype()
    proto.register("python-001", site1)
    site2 = proto.clone(
        "python-001",
        name="Python Package Index",
        domain="pypi.org",
        description="Repository for published packages",
        category="Open Source Software",
    )
    for site in (site1, site2):
        print(site)
if __name__ == "__main__":
    main()
