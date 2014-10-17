"""
The 1st test project on github to learn how to collaborate, created by Jia Lia & Guanglin Du.
Oct. 15, 2014 Wed.
"""

class HelloGithub(object):
	
	def __init__(self):
		self.name = "github"

		
	def hello_github(self):
		print("hello, github. From goodmaoxixi on Oct. 15. 2014 Wed.")

	
	def say_something(self, name = "github"):
		self.name = name
		print("Hello, %s!" % self.name)

		
	def sum(self):
		a = 1
		b = 2
		sum = a + b
		print("a, b, sum = %i, %i, %i" % (a, b, sum))
		
		
if __name__ == '__main__':
	hg = HelloGithub()
	hg.hello_github()
	hg.say_something()
	hg.sum()
	
