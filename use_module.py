# Aug. 9, 2014 Sat.
# Created by Xiaoyun Du.

# Use a module(a .py file)
import square_equation_root
import calculator
import class_people

a, b, c = 3.0, 4.0, 5.0 # parallel assignment 
square_equation_root.square_equation_root2(a, b, c)

jump = calculator.Calculator(90)
jump.add(10)
print(jump.get_current())

p1 = class_people.People()
print("The eye color is %s." % p1.get_eye_color())
