# Uses python3
import sys
import numpy as np
def optimal_weight(W, w):
    # write your code here
    n = len(w)
    D= np.zeros((n+1, W+1))

    for i in range(1, n+1):
        for j in range(1, W+1):
            D[i, j] = D[i-1, j]
            if w[i-1] <= j:
                temp = D[i-1, j-w[i-1]] + w[i-1]
                if temp >= D[i, j]:
                    D[i, j] = temp
    return int(D[-1, -1])
        

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
