import os
from cudatext import *
from .maps import MAP

def make_fn(fn0, fn1, ext):
    return os.path.join(os.path.dirname(fn0), fn1+'.'+ext)

class Command:
    def run(self):
        fn0 = ed.get_filename()
        if not fn0: return
        fn1 = os.path.basename(fn0)
        n = fn1.rfind('.')
        if n<=0: return
        ext1 = fn1[n+1:]
        fn1 = fn1[:n]
        
        fn2 = ''
        if ext1 in MAP.keys():
            ext2 = MAP[ext1]
            if type(ext2) is str:
                fn2 = make_fn(fn0, fn1, ext2)
            elif type(ext2) is tuple:
                for e in ext2:
                    fn2a = make_fn(fn0, fn1, e)
                    if os.path.isfile(fn2a):
                        fn2 = fn2a
                        break
        
        if os.path.isfile(fn2):
            file_open(fn2)
        else:
            msg_status('Cannot switch file')
