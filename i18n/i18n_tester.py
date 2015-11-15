# Nov. 15, 2015 Sun.
# Used to test module i18n_util.py.
# What is the best way to internationalize a Python app with multiple i18n domains?
# http://stackoverflow.com/questions/694768/what-is-the-best-way-to-internationalize-a-python-app-with-multiple-i18n-domains

class I18nTester(object):
    """Defines a class to simulate a simple calculator"""
    def __init__(self):
        """The constructor"""
        self.result = 0 # defines a variable
        self.greeting = "Hello, Python!"
    
    def add(self, amount):
        """Defines a method of the class"""
        # add number to result
        self.result += amount
    
    def get_result(self):
        """Returns the value of variable result"""
        return self.result
