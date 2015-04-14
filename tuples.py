# Jun. 21, 2014 Sat.
# See http://www.afterhoursprogramming.com/tutorial/Python/Introduction/
# Various tutorials: https://wiki.python.org/moin/BeginnersGuide/Programmers

myList = [1, 2, 3]
myList.append(4)
print(myList)

myTuple = (1, 2, 3)
print(myTuple)
print myTuple[0]
print myTuple[2]

myTuple2 = (1, 2, 3)
myList2 = list(myTuple2)
#myTuple2.append(4) # tuples are immutable
#print(myTuple2)
myList2.append(4)
print(myList2)
