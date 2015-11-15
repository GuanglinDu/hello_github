# Jun. 21, 2014 Sat.
# See http://www.afterhoursprogramming.com/tutorial/Python/Introduction/
# Various tutorials: https://wiki.python.org/moin/BeginnersGuide/Programmers

# The string class is str in Python
mystr = ""
print(type(mystr))

mystr2 = str()
print(type(mystr2))

mystr2 += "Hello, str objects" # appends
print(mystr2)

mystr2 = ", ".join(["hello", "str!"])
print(mystr2)

# The last element is excluded
a = "string"
print(a[1:3]) # tr
print(a[:-1]) # strin
print(a[:-3]) # str
print(a[:2]) # st
print(a[2:-2]) # ri

