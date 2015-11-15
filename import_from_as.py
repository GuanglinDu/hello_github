# Created on Apr 17, 2015 Fri.
# Showcases import ... from ... as
# http://stackoverflow.com/questions/9439480/from-import-vs-import

# It depends on how you want to access the import when you refer to it.

#from urllib import request
# access request directly.
#mine = request()

#import urllib.request
# used as urllib.request
#mine = urllib.request()

# You can also alias things yourself when you import for simplicity or to avoid masking built ins:
#from os import open as open_
# lets you use os.open without destroying the 
# built in open() which returns file handles.

# Import method say_hi from module bar in package foo
from foo.bar import say_hi
say_hi()

# Import method add from module bar in package foo and alias it to sum01
from foo.bar import add as sum01
sum01(1, 2)

