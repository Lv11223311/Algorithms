# python 3
import numpy as np

def fib(n):
    F = [0] * (n+1)
    if n <= 1:
        return n
    F[0] = 0
    F[1] = 1
    for i in range(2, n+1):
        F[i] = F[i -1] + F[i - 2]
    return F[n]

if __name__ == "__main__":
    input_n = int(input())
    print(fib(input_n))