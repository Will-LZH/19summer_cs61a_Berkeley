def if_f(cond):
    if cond:
        return lambda a, b: a
    else:
        return lambda a, b: b

def factorial(n):
    def base():
        return 1
    def recursive():
        return n*factorial(n-1)
    return if_f(n!=0)(recursive(),base())