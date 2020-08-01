from Timer_Func.timer_func import TimePassed


def fibi(n):
    """Fibonacci numbers using loop functions"""
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old + new
    return new


def fib(n):
    """Fibonacci numbers using recursive function"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


memo = {0: 0, 1: 1}  # create a memory for the fibm function # it makes it millions times faster then fib n function


def fibm(n):
    """Fibonacci numbers using a memory allocation"""
    if n not in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]


class Fibonacci:
    """Fibonacci computation class"""
    def __init__(self, i1= 0, i2=0):
        self.memo = {0:i1, 1:i2}

    def __call__(self, n):
        if n not in self.memo:
            self.memo[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.memo[n]

