#importingF2.py
print('in importing F2.py')
from importingF1 import *
func1()

def func2():
    import importingF1
    importingF1.func1()

func2()