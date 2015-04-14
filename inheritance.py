#!/usr/bin/python

# Jun. 21, 2014 Sat.
# See http://www.tutorialspoint.com/python/python_classes_objects.htm

class Parent: # define parent class
    parentAttr = 100
    def __init__(self):
        print "Calling parent constructor"

    def parentMethod(self):
        print 'Calling parent method'

    def setAttr(self, attr):
        Parent.parentAttr = attr
        print "Setting parent attr: ", attr

    def getAttr(self):
        print "Parent attribute :", Parent.parentAttr
    
    def myMethod(self):
        print 'Calling parent method'

class Child(Parent): # define child class
    def __init__(self):
        print "Calling child constructor"

    def childMethod(self):
        print 'Calling child method'
    
    # Overriding methods    
    def myMethod(self):
        print 'Calling child method'

c = Child()                    # instance of child
c.childMethod()            # child calls its method
c.parentMethod()         # calls parent's method
c.setAttr(200)             # again call parent's method
c.getAttr()                    # again call parent's metho
c.myMethod()

