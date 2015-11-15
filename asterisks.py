# https://www.technovelty.org/python/on-asterisks-in-python.html
# Create on Jul. 25, 2015 Sat.

print("--- ordinary object + tuple + dictinary ---")
def myfunction(arg, *vargs, **kargs):
    print arg
    print type(arg)
    
    print("")
    print vargs
    print type(vargs)
    
    print("")
    print kargs
    print type(kargs)

myfunction(1, 2, 3, 4, 5, test1="abc", test2="def")
# 1
# (2, 3, 4, 5)
# {'test1': 'abc', 'test2': 'def'}


# Args are composed of a tuple object and a dictionary object
print("\n--- tuple + dictinary ---")
def myfunction2(*vargs, **kargs):
    print vargs
    print kargs

myfunction2(10, 11, key1="abc2", key2="def2") # a list + a dictinary
myfunction2(10, 11) # a tuple only
myfunction2(key1="abc2", key2="def2") # a dictionary only
