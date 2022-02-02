import os, sys
from stat import *

def get_stat(file):
    return os.stat(file).st_size

def walktree(top, callback, sizes):
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            walktree(pathname, callback, sizes)
        elif S_ISREG(mode):
            sizes.append(callback(pathname))
        else:
            print('Skipping %s' % pathname)


if __name__== "__main__":
    file_path = './my_project/'
    sizes=[]
    walktree(file_path, get_stat, sizes)
    res = {'10': 0, '100': 0, '1000': 0, '10000': 0}

    for i in sizes:
        if i >=10 and i<100:
            res['10'] += 1
        elif i >=100 and i<1000:
            res['100'] += 1
        elif i >=1000 and i<10000:
            res['1000'] += 1
        elif i >=10000:
            res['10000'] += 1
    print(res)
