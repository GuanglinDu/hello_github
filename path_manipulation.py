# Manipulations of paths
# Created on Apr 10, 2015 Fri.

import os, sys

current_path = os.path.dirname(os.path.abspath(__file__))
python_path = os.path.abspath( os.path.join(current_path, os.pardir, 'python27', '1.0'))
noarch_lib = os.path.abspath( os.path.join(python_path, 'lib', 'noarch'))

# The variable sys.path is a list of strings that determines the interpreter's search path
# for modules. It is initialized to a default path taken from the environment variable
# PYTHONPATH, or from a built-in default if PYTHONPATH is not set. 
sys.path.append(noarch_lib)

def print_info():
    print("__name__ = %s" % __name__)
    print("__file__ = %s" % __file__)
    print("current_path = %s" % current_path)
    print("python_path = %s" % python_path)    
    print("noarch_lib = %s" % noarch_lib)    
    print("Sys.path = %s" % sys.path)

# Call the function
if __name__ == '__main__':
    print_info()
