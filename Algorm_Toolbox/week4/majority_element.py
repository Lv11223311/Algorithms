# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    D = {}
    for i in range(right):
        if a[i] not in D:
            D[a[i]] = 1
        else:
            D[a[i]] += 1
    for i in D.keys():
        key = D.get(i)
        if key > right/2:
            return i
    return -1



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
