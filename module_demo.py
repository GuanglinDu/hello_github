"""
module_demo.py
To demonstrate the use of a Python module.
Created by DGL on Oct. 17, 2014 Fri.
"""

# Import a module
import hello_github

class ModuleDemo(object):
	def __init__(self, name):
		self.name = name
		self.hgb = hello_github.HelloGithub()

	
	def hello_module(self):
		print("Hi, in Python a module is a Python file!")
	
	
	def hi_github(self):
			self.hgb.hello_github()
		

if __name__ == '__main__':
	md = ModuleDemo("lijia")
	md.hello_module()
