# http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/ 
# A variable length arguments demo
# The special syntax, *args and **kwargs in function definitions is used to pass a variable number of arguments to a function. The single asterisk form (*args) is used to pass a non-keyworded, variable-length argument list, and the double asterisk form is used to pass a keyworded, variable-length argument list. Here is an example of how to use the non-keyworded form. This example passes one formal (positional) argument, and two more variable length arguments.

def test_var_args(farg, *args):
    print "formal arg:", farg

    print("The type of args is %s" % type(args))
    for arg in args:
        print "another arg:", arg

test_var_args(1)
print ""
test_var_args(1, "two")
print ""
test_var_args(1, "two", 3)

# Here is an example on how to use the keyworded form.
# Again, one formal argument and two keyworded variable arguments are passed.

def test_var_kwargs(farg, **kwargs):
    print "formal arg:", farg
    for key in kwargs:
        print "another keyword arg: %s = %s" % (key, kwargs[key])

test_var_kwargs(farg=1, myarg2="two", myarg3=3)

# Results:
# formal arg: 1
# another keyword arg: myarg2: two
# another keyword arg: myarg3: 3
