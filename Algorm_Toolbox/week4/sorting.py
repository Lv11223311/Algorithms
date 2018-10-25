# Uses python3
import sys
import random

def quicksort(arr, left, right):
    # 只有left < right 排序
    if left < right:
        # pivot_index = partition(arr, left, right)
        random_index = random.randint(left, right)
        arr[left], arr[random_index] = arr[random_index], arr[left]
        pivot = arr[left]
        lt = left # arr[left+1...lt] < v
        gt = right + 1 # arr[gt...right] > v
        i = left + 1 # arr[lt+1...i] == v
        while i < gt:
            if arr[i] < pivot:
                arr[i], arr[lt+1] = arr[lt+1], arr[i]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt-1] = arr[gt-1], arr[i]
                gt -= 1
            else:
                i += 1
        arr[left], arr[lt] = arr[lt], arr[left]
        quicksort(arr, left, lt-1)
        quicksort(arr, gt, right)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    quicksort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
