def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)
    
def fib(x):
    if x <= 1:
        return x
    else: 
        return fib(x-1) + fib(x-2)
    
def is_fib(n, a = 0, b = 0):
    if n < 0:
        return False
    if n == a:
        return True
    if n < a:
        return False
    
    return is_fib(n, b, a + b)