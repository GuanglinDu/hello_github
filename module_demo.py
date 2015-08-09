"""module_demo.py
Demonstrate how to use of a Python module.
Created by DGL on Oct. 17, 2014 Fri.
"""

# Imports a whole module only. Qualifies its members when used.
import hello_github
# Imports only a variable from a module so as to use it directly
from hello_github import hello
# Imports a module bar from package (subfolder) foo
import foo.bar

class ModuleDemo(object):
    def __init__(self, name):
        self.name = name
        self.hgb = hello_github.HelloGithub()

    
    def hello_module(self):
        print("Hi, in Python a module is a Python file!")
        #print("A variable imported from module hello_github: %s" % hello_github.hello) # qualify with the module name
        # Uses the imported variable hello directly without qualifying it with the module name
        print("A variable imported from module hello_github: %s" % hello)
    
    
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

