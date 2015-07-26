# Shows the built-in method getattr
# See https://docs.python.org/2/library/functions.html?highlight=getattr#getattr
import os

__file__ = os.path.abspath(__file__)
print("__file__ = %s" % __file__)

# To support link files, such as desktop shortcut?
if os.path.islink(__file__):
    __file__ = getattr(os, 'readlink', lambda x: x)(__file__)
    print("__file__ = %s" % __file__)
else:
    print("A non-link file")
