# Jun. 21, 2014 Sat.
# See http://www.afterhoursprogramming.com/tutorial/Python/Introduction/
# Various tutorials: https://wiki.python.org/moin/BeginnersGuide/Programmers

# 3 ways to create a list object. This applies to dict, too (tuple?)
# Way 1: creates on with give values using the square brackets
print("--- Way 1: creates on with give values using the square brackets ---")
list01 = [1, 2, 3, 4, 5]
print(list01[1])

list01.append(10)
list01.append(11)
list01.insert(0, -1) # insert as the first entry

for a in list01:
    print(a)

# Way 2: creates an empty list object and then populate it
print("--- Way 2: creates an empty list object and then populate it ---")
list02 = []
list02.append(20)
list02.insert(0, 21)
print list02

for a in list02:
    print(a)

# Way 3: creates a list object with the class name list explicitly
print("--- Way 3: creates an empty list object and then populate it ---")
list03 = list() # 
list03.append(31)
list03.insert(0, 30)
for a in list03:
    print(a)

