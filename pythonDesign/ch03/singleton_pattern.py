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
