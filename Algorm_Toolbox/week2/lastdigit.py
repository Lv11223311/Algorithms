# Uses python3
import sys

import numpy as np

def fib(n):
    F = [0] * (n+1)
    if n <= 1:
        return n
    F[0] = 0
    F[1] = 1
    for i in range(2, n+1):
        F[i] = (F[i -1] + F[i - 2]) % 10
    return F[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib(n))