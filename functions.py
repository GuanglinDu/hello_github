# Global
a = 10

def some_function():
    """A simple function commentary"""
    print("boo")

def some_function2(a, b):
    """Another simple function commentary"""
    print(a + b)
    c = a + b
    print('a + b = %i' % c)
    print('a + b = %i' % (a+b))    
    print('a + b = %f' % 123.44)
    print('a + b = %.2f' % 123.444)

some_function()
print(a)

some_function2(12, 451)

a = 'abcdefxy'
print('%.5s' % a)
