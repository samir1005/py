import os


import os, sys

os.chdir('Path')
for f in os.listdir('Path'):
    file_name, file_ext = os.path.splitext(f)
    ext = '.mp4'
    new = '{}'.format(file_name + ext)
    os.rename(f, new)
    print (f)





