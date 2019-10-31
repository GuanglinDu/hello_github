# Created on Oct 31, 2019 Thu
# https://www.mkyong.com/python/python-how-to-list-all-files-in-a-directory/

import os

path = 'd:\\tmp\\test\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file.lower():
            files.append(os.path.join(r, file))

for f in files:
    print(f)
