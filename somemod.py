def _myhelper(x):
    return x * 2

def myfunc1(x):
    result = _myhelper(x)
    return result

def myfunc2(x):
    result = _myhelper(x) * 2
    return result