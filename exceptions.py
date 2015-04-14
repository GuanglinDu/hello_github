# Jun. 21, 2014 Sat.
# See http://www.afterhoursprogramming.com/tutorial/Python/Introduction/
# Various tutorials: https://wiki.python.org/moin/BeginnersGuide/Programmers

var1 = "1"

# Only error prompt
try:
    var1 = var1 + 1
except:
    print("Error: ", var1, " is not a number")
print("var1 is a string and equals %s" % var1)

# Do something
try:
    var2 = var1 + 1
except:
    var2 = int(var1) + 1
print("var2 is %i" %    var2)
