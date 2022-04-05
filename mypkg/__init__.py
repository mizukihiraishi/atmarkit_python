print(__name__)
#from mypkg.mymath import fact, fizzbuzz, fib
#from mypkg.greet import hello
from .mymath import fact, fizzbuzz, fib
from .greet import hello

__all__ = ['fact', 'fizzbuzz', 'fib', 'hello']