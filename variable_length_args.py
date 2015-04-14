# http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/ 
# A variable length arguments demo
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

