# http://stackoverflow.com/questions/4103667/python-ternary-operator
# foo = "True" if test else "False"
# Created on Jul. 26, 2015 Sun.

a = 0
b = 1
c = 2

foo = "True" if a == b else "False"
print(foo) # False

d = c if a else b
print(d) # 1

