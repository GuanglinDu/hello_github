# Create on Aug. 1, 2015 Sat
# See 5.1. Truth Value Testing,  https://docs.python.org/2/library/stdtypes.html?highlight=list#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange
# The following values are considered false:
# None
# False
# zero of any numeric type, for example, 0, 0L, 0.0, 0j.
# any empty sequence, for example, '', (), [].
# any empty mapping, for example, {}.
# instances of user-defined classes, if the class defines a __nonzero__() or __len__() method, when that method returns the integer zero or bool value False. [1]
# All other values are considered true - so objects of many types are always true.
def is_true(arg):
    if arg:
        print("arg is true")
    else:
        print("arg is false")

false_values = [None, False, 0, (), [], {}]
for a in false_values:
    is_true(a)


