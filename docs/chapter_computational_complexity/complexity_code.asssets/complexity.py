"""
Code for Complexity
"""
from viztracer import VizTracer

def fib(n: int) -> int:
    if n <= 2:
        return 1    
    return fib(n - 1) + fib(n - 2)

with VizTracer():
    fib(10)