def return_more_than_one():
    a, b = 2, 3
    return a, b

def ip_string_to_num(s):
    """Converts a dotted IPv4 address to its integer form.
    Example:
    10.0.0.1 -> 1010.00000000.00000000.00000001 ->
    1010000000000000000000000001 -> 167772161
    """
    return reduce(lambda a, b: a << 8 | b, map(int, s.split(".")))
    
a, b = return_more_than_one()
print("a, b = %d, %d" % (a, b))

s = "10.0.0.1"
ip = ip_string_to_num(s)
print(" The type of ip: %s, %d" % (type(ip), ip))


