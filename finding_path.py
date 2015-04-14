# http://stackoverflow.com/questions/10025863/os-path-abspathfile1-txt-doesnt-return-the-correct-path
# os.path.abspath(filename) returns an absolute path as seen from your current working directory. It does no checking whether the file actually exists.
# If you want the absolute path of /home/bentley4/Desktop/sc/file1.txt and you are in /home/bentley4 you will have to use os.path.abspath("Desktop/sc/file1.txt").

import os

my_path = os.path.abspath('finding_path.py')
print "my_path = %s" % (my_path)

# http://stackoverflow.com/questions/9271464/what-does-the-file-wildcard-mean-do
# __file__ is the name of the current file, like main.py.
global __file__
print "__file__ = %s" % (__file__)
__file__ = os.path.abspath(__file__)
print "__file__ = %s" % (__file__)
aTuple = os.path.splitext(__file__) # returns a tuple
print type(aTuple)
print aTuple
print aTuple[0]

print os.path.join(os.path.dirname(__file__), '..')
print os.path.dirname(os.path.realpath(__file__))
print os.path.abspath(os.path.dirname(__file__))
