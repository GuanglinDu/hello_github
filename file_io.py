# Aug. 8, 2014 Fir.
# Created by Xiaoyun Du. 

f = open("test.txt","r") #opens file with name of "test.txt"
print(f.read(1))
print(f.read())
f.close()

f = open("test.txt","r") #opens file with name of "test.txt"
print(f.readline())
print(f.readline())
f.close()

f = open("test.txt","r") #opens file with name of "test.txt"
contents = f.read()
f.close()
print("Type of contents: %s" % type(contents))
print(contents)

lines = contents.splitlines()
print("Type of lines: %s" % type(lines))


