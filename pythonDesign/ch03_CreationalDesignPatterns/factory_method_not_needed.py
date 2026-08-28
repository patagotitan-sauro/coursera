#!/home/rouse/Scrips/pythonDesign/.venv_coursera/bin/python
"""
ch03/factory/factory_method_not_needed.py
To show how one could deal with simple use cases without the factory method pattern, an alternative implementation has been provided in the ch03/factory/factory_method_not_needed.py file. As you can see, there is no more factory. And the following extract from the code shows what we mean when we say that in Python, you just create objects where you need them, without an intermediary function or class, which makes your code more Pythonic:

"""
import json
import xml.etree.ElementTree as ET
from pathlib import Path


class JSONDataExtractor:
   def __init__(self, filepath: Path):
       self.data = {}
       with open(filepath) as f:
           self.data = json.load(f)

   @property
   def parsed_data(self):
       return self.data

class XMLDataExtractor:
   def __init__(self, filepath: Path):
       self.tree = ET.parse(filepath)

   @property
   def parsed_data(self):
     return self.tree

def extract(case: str):
    dir_path = Path(__file__).parent
    if case == "json":
        path = dir_path / Path("movies.json")
        data = JSONDataExtractor(path).parsed_data
        print(data)

if __name__ == '__main__':
    extract(case='json')
