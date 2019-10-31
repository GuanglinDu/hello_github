# Created on Oct 31, 2019 Thu
# To remove the 0 bytes photos.
  
import os 


def delete_emtpy_file(topdir):
    for filename in os.listdir(topdir):
        bytes = os.path.getsize(filename)
        if bytes < 0.0001:
            print("{0}, {1}".format(filename, bytes))
            os.remove(filename) 


# Delete jpg/png files with 0 bytes reccursively.
def delete_emtpy_file2(topdir):
    files = []
    count = 0
    # r=root, d=directories, f=files
    for r, d, f in os.walk(topdir):
        for file in f:
            if ('.jpg' in file.lower()) or ('.png' in file.lower()):
                #files.append(os.path.join(r, file))
                file_abs_name = os.path.join(r, file)
                bytes = os.path.getsize(file_abs_name)
                if bytes < 0.0001:
                    print("{0}, {1}".format(file_abs_name, bytes))
                    os.remove(file_abs_name)
                    count += 1                  
                
    #for f in files:
    #    print(f)
    print("Removed {0} zero bytes jpg/png files form {1}!".format(count, topdir))
                
if __name__ == '__main__':
    #topdir = "D:\\tmp\\test\\01"
    topdir = "H:\\Pictures\\2015"
    delete_emtpy_file2(topdir) 
 
