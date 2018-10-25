# Uses python3
import sys
import numpy as np
def get_optimal_value(n,capacity, weights, values):
    value = 0.
    # write your code here
    density = [i/k for i, k in zip(values, weights)]
    l = [i for i in zip(density, zip(values, weights))]
    l = sorted(l, key=lambda t:t[0],reverse=True)
    keys = [i[1] for i in l]
    values, weights = zip(*keys)
    weights =list(weights)
    values = list(values)
    for i in range(n):  
        if capacity == 0:
            return value
        a = min(weights[i], capacity)
        value += a * (values[i] / weights[i])
        weights[i] -= a
        capacity -= a
    return value
    


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.10f}".format(opt_value))