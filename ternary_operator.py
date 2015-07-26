# http://stackoverflow.com/questions/4103667/python-ternary-operator
# foo = "True" if test else "False"

a = 0
b = 1
c = 2

foo = "True" if a == b else "False"
print(foo)

d = c if a else b # 1
print(d)

