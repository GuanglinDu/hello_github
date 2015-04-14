# Jun. 21, 2014 Sat.
# See http://www.afterhoursprogramming.com/tutorial/Python/Introduction/
# Various tutorials: https://wiki.python.org/moin/BeginnersGuide/Programmers

myDict = {'someItem': 2, 'otherItem': 20}
print(myDict['otherItem'])

myDict['newItem'] = 400
for a in myDict:
    print(a)

for a in myDict:
    print(a, myDict[a])
