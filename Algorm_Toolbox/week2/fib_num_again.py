# using python3 
import sys

def fib_again(n, m):
    F = [0] * (n+1)
    if n <= 1:
        return n
    F[0] = 0
    F[1] = 1
    for i in range(2, n+1):
        F[i] = (F[i -1] + F[i - 2]) % m
    return F[n]




if __name__ == "__main__":
    input = sys.stdin.read()
    tokens = input.split()
    n = int(tokens[0])
    m = int(tokens[1])
    print(fib_again(n, m))