# Jun. 5, 2014 Sat.
# See Scoping and use of the 'global' keyword in Python, https://stereochro.me/ideas/global-in-python
# If you specifically want to be able to change the value a given variable
# in the global scope contains, then use the global keyword.

foo = 0

def bar():
    global foo
    print "Entering bar(), foo is", foo
    foo += 1
    print "Leaving bar(), foo is", foo

bar()
print "And in the module scope, foo is", foo
