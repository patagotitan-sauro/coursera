#!/home/rouse/Scrips/coursera/pythonDesign/.venv/bin/python
"""
The Singleton Pattern
The basic idea is that only one instance of a particular class, doing a job, is created for the needs of the program.
To ensure that this works, we need mechanisms that prevent the instantiation of the class more than once and also prevent cloning.

# Use Cases for the Singleton Pattern
The singleton design pattern is useful when you need to create only one object or you need some sort of object capable of maintaining
a global state for your program. Other possible use cases are the following:
    (i) Controlling concurrent access to a shared resource-for example, the class managing the connection to a database
    (ii) A service or resource that is transversal in the sense that it can be accessed from different parts of the application or
        by different users and do its work-for example, the class at the core of a logging system or utility
# Implementing the Singleton Pattern
As discussed, the singleton pattern ensures that a class has only one instance and provides a global point to access it.
In this example, we'll create a URLFetcher class that fetches content from web pages. We want to ensure that only one
instance of this class exists to keep track of all fetched URLs.
"""
import urllib.request

class URLFetcher:
    def __init__(self):
        self.urls = []
    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                page_content = response.read()
                with open("content.html", "a") as f:
                    f.write(page_content + "")
                self.urls.append(url)

print(URLFetcher() is URLFetcher()) # will return False, as we are creating two 
#different instances of the class

# This output shows that the class in this version does not yet respect the singleton 
# pattern. To make it a singleton, we'll use the metaclass technique.
# Info: A metaclass in Python is a class of a class that defines how a class behaves. 
# We'll create a SingletonType metaclass that ensures that only one instance 
# of URLFetcher exists, as follows:


class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            obj = super(SingletonType, cls).__call__(*args, **kwargs)
            cls._instances[cls] = obj
        return cls._instances[cls]

# Now, we modify our URLFetcher class to use this metaclass, as follows:

class URLFetcher(metaclass=SingletonType):
    def __init__(self):
        self.urls = []
    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                page_content = response.read()
                with open("content.html", "a") as f:
                    f.write(str(page_content))
                self.urls.append(url)

# Finally we create the main
def main():
    my_urls = [
        "http://python.org",
        "https://planetpython.org/",
        "https://www.djangoproject.com/",
    ]

    print(URLFetcher() is URLFetcher())
    fetcher = URLFetcher()
    for url in my_urls:
        fetcher.fetch(url)
    print(f"Done URLs: {fetcher.urls}")
if __name__ == "__main__":
    main()

"""
Here is a summary of what we do in the code:

    We start with our needed module imports (urllib.request).
    We define a SingletonType class, with its special call() method.
    We define URLFetcher, the class implementing the fetcher for the web pages, 
initializing it with the urls attribute; as discussed, we add its fetch() method.
    Lastly, we add our main() function, and we add Python's conventional snippet 
used to call it.

Should You Use the Singleton Pattern?

While the singleton pattern has its merits, it may not always be the most Pythonic 
approach to managing global states or resources. Our implementation example worked, but if we 
stop a minute to analyze the code again, we notice the following:

    The techniques used for the implementation are rather advanced and not easy to explain
to a beginner
    By reading the SingletonType class definition, it is not easy to immediately see that 
it provides a metaclass for a singleton if the name does not suggest it.

In Python, developers often prefer a simpler alternative to singleton: using a module-level 
global object.

`Note`: Python modules act as natural namespaces that can contain variables, functions, 
and classes, making them ideal for organizing and sharing global resources. 
"""
# https://python-patterns.guide/python/module-globals/
