"""
module_demo.py
To demonstrate the use of a Python module.
Created by DGL on Oct. 17, 2014 Fri.
"""

# Import a module
import hello_github
from hello_github import hello
# Import module bar from subfolder foo
import foo.bar

class ModuleDemo(object):
    def __init__(self, name):
        self.name = name
        self.hgb = hello_github.HelloGithub()

    
    def hello_module(self):
        print("Hi, in Python a module is a Python file!")
        print("A variable imported from the moule: %s" % hello) # imported variable
    
    
    def hi_github(self):
        self.hgb.hello_github()
        self.hgb.sum()
    
    def module_in_subfolder(self):
       foo.bar.say_hi() 

if __name__ == '__main__':
    md = ModuleDemo("lijia")
    print("--- Call method hello_module ---");
    md.hello_module()
    
    print("\n--- Call method hi_github ---");
    md.hi_github()

    print("\n--- Call method say_hi in module bar of package foo ---");
    md.module_in_subfolder()

