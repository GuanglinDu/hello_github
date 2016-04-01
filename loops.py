# Transforming Code into Beautiful, Idiomatic Python
# https://www.youtube.com/watch?v=OSGv2VnC0go

print('--- Looping over a range of numbers ---')

for i in [0, 1, 2, 3, 4, 5]:
    print i**2

# better
for i in range(6):
    print i**2

# best
for i in xrange(6):
    print i**2


print('--- Looping over a collection ---')

colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print colors[i]

# The Python way
for color in colors:
    print color


print('--- Looping backwards ---')

for i in range(len(colors)-1, -1, -1):
    print colors[i]

# The Python way
for color in reversed(colors):
    print color


print('--- Looping over a collection and indicies ---')

for i in range(len(colors)):
    print i, '-->', colors[i]
    
# The Python way
for i, color in enumerate(colors):
    print i, '-->', colors[i]


print('--- Looping over two collections ---')
names = ['raymond', 'rachel', 'matthew']
n = min(len(names), len(colors))
for i in range(n):
    print names[i], '-->', colors[i]
    
# The Python way
for name, color in zip(names, colors):
    print name, '-->', color

# Better (Python 3 only)
#for name, color in izip(names, colors):
#    print name, '-->', color


print('--- Looping in sorted order ---')
for color in sorted(colors):
    print color

for color in sorted(colors, reverse=True):
    print color


print('--- Custom sort order ---')

print('--- Call a functiion until a sentinel value (12:18) ---')